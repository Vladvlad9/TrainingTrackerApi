from pydantic import UUID4
from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from src.exceptions import ObjectAlreadyExistError, ObjectNotFoundError
from src.databse.alchemy.models import Workout
from src.repos.alchemy import WorkoutRepo, WorkoutExerciseRepo
from src.types import WorkoutCreateDTO, WorkoutBaseDTO, WorkoutExerciseDTO, WorkoutUpdateDTO

__all__ = ["WorkoutService"]


class WorkoutService:
    def __init__(self, session: AsyncSession):
        self._session = session
        self._workout_repo = WorkoutRepo(session=session)
        self._workout_exercise_repo = WorkoutExerciseRepo(session=session)

    async def get(self):
        pass

    async def _get_workout_with_exercises(self, workout_id: UUID4) -> Workout:
        workout = await self._workout_repo.get(
            filters=[Workout.id == workout_id],
            options=[selectinload(Workout.workout_exercises)],
        )
        if workout is None:
            raise ObjectNotFoundError(name="workout")
        return workout

    @staticmethod
    def _to_workout_base_dto(workout: Workout) -> WorkoutBaseDTO:
        return WorkoutBaseDTO(
            id=workout.id,
            title=workout.title,
            note=workout.note,
            scheduled_at=workout.scheduled_at,
            status=workout.status,
            exercises=[
                WorkoutExerciseDTO(
                    exercise_id=exercise.exercise_id,
                    sets=exercise.sets,
                    reps=exercise.reps,
                    weight=exercise.weight,
                    duration_minutes=exercise.duration_minutes,
                )
                for exercise in workout.workout_exercises
            ],
        )

    async def post(self, data: WorkoutCreateDTO) -> WorkoutBaseDTO:
        workout_data = data.model_dump()
        exercises_data = workout_data.pop("exercises", [])

        try:
            workout = await self._workout_repo.add_flush_refresh_one(obj=workout_data)
        except IntegrityError:
            await self._session.rollback()
            raise ObjectAlreadyExistError(name="workout")

        try:
            for exercise in exercises_data:
                await self._workout_exercise_repo.add_flush_refresh_one(
                    obj={**exercise, "workout_id": workout.id},
                )

            workout_from_db = await self._get_workout_with_exercises(workout_id=workout.id)

            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise ObjectAlreadyExistError(name="workout_exercise")

        return self._to_workout_base_dto(workout=workout_from_db)

    async def patch(self, workout_id: UUID4, data: WorkoutUpdateDTO) -> WorkoutBaseDTO:
        await self._get_workout_with_exercises(workout_id=workout_id)

        update_data = data.model_dump(exclude_unset=True, exclude_none=True)

        try:
            if update_data:
                await self._session.execute(
                    update(Workout).where(Workout.id == workout_id).values(**update_data)
                )
            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise ObjectAlreadyExistError(name="workout")

        workout_from_db = await self._get_workout_with_exercises(workout_id=workout_id)
        return self._to_workout_base_dto(workout=workout_from_db)

    async def delete(self, workout_id: UUID4):
        workout = await self._session.get(Workout, workout_id)
        if not workout:
            raise ValueError(f"Workout with id {workout_id} not found")

        await self._session.delete(workout)
        await self._session.commit()

    async def list(self):
        pass
