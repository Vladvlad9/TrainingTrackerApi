from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.exceptions import ObjectAlreadyExistError
from src.repos.alchemy import WorkoutRepo, WorkoutExerciseRepo

__all__ = ["WorkoutService"]

from src.types import WorkoutCreateDTO


class WorkoutService:
    def __init__(self, session: AsyncSession):
        self._workout_repo = WorkoutRepo(session=session)
        # self._workout_exercise_repo = WorkoutExerciseRepo(session=session)

    async def get(self):
        pass

    async def post(self, data: WorkoutCreateDTO):

        print("data:", data)

        workout_data = data.model_dump()
        exercises_data = workout_data.pop("exercises", [])
        print("workout_data:", workout_data)

        print("exercises_data:", exercises_data)
        try:
            workout = await self._workout_repo.insert(obj=workout_data)
        except IntegrityError:
            raise ObjectAlreadyExistError(name="workout")

        # for exercise in exercises:
        #     await self._workout_exercise_repo.insert(
        #         obj={**exercise, "workout_id": workout.id},
        #     )
        #
        # return workout

    async def patch(self):
        pass

    async def delete(self, workout_id: UUID4):
        pass

    async def list(self):
        pass
