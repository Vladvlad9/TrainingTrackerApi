from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.exception_handlers.factory import ExceptionHandlerFactory
from api.exceptions import ObjectExistsException, InternalServerException, ObjectNotFoundException
from src.databse.alchemy.models import Exercise
from src.exceptions import ObjectAlreadyExistError, ObjectNotFoundError
from src.services import ExerciseService

from src.types import (
    ExerciseCreateRequestDTO,
    ExerciseFilterDTO,
    Paginator,
    ExerciseDetailResponseDTO
)

__all__ = ["RESTExerciseService"]

exercise_exception_handler = ExceptionHandlerFactory(
    exc_mapping={
        ObjectAlreadyExistError: ObjectExistsException(name="exercise"),
        ObjectNotFoundError: ObjectNotFoundException(name="exercise"),
    },
    default_exc=InternalServerException(name="Exercise"),
)


class RESTExerciseService:
    def __init__(self, session: AsyncSession):
        self._exercise_service = ExerciseService(session=session)

    async def list(self, page: int, page_size: int, filters: ExerciseFilterDTO) -> Paginator[ExerciseDetailResponseDTO]:
        return await self._exercise_service.list(page=page, page_size=page_size, filters=filters)

    @exercise_exception_handler()
    async def get(self, exercise_id: UUID) -> ExerciseDetailResponseDTO:
        return await self._exercise_service.get(exercise_id=exercise_id)

    @exercise_exception_handler()
    async def post(self, data: ExerciseCreateRequestDTO) -> Exercise:
        return await self._exercise_service.post(data=data)
