from math import ceil
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import Exercise
from src.exceptions import ObjectNotFoundError, ObjectAlreadyExistError
from src.repos.alchemy import ExerciseRepo

from src.types import (
    ExerciseCreateRequestDTO,
    ExerciseDetailResponseDTO,
    Paginator,
    Pagination,
    ExerciseFilterDTO
)

__all__ = ["ExerciseService"]


class ExerciseService:
    def __init__(self, session: AsyncSession):
        self._repo = ExerciseRepo(session=session)

    async def get(self, exercise_id: UUID) -> ExerciseDetailResponseDTO:
        exercise = await self._repo.get(filters=[Exercise.id == exercise_id])
        if not exercise:
            raise ObjectNotFoundError(name="Exercise")

        return ExerciseDetailResponseDTO.model_validate(obj=exercise)

    async def post(self, data: ExerciseCreateRequestDTO) -> Exercise:
        try:
            return await self._repo.insert(obj=data.model_dump())
        except IntegrityError as e:
            raise ObjectAlreadyExistError(name="exercise")

    async def list(self, page: int, page_size: int, filters: ExerciseFilterDTO) -> Paginator[ExerciseDetailResponseDTO]:
        count = await self._repo.count()
        filter_conditions = []

        if filters.category is not None:
            filter_conditions.append(Exercise.category == filters.category)

        if filters.muscle_group is not None:
            filter_conditions.append(Exercise.muscle_group == filters.muscle_group)

        exercises = await self._repo.list_data(
            page=page,
            page_size=page_size,
            filters=[*filter_conditions] if filter_conditions else None,
        )

        return Paginator(
            results=[ExerciseDetailResponseDTO.model_validate(obj=exercise) for exercise in exercises],
            pagination=Pagination(
                page_size=page_size,
                page=page,
                page_count=ceil(count / page_size) if count > 0 else 1,
            ),
        )
