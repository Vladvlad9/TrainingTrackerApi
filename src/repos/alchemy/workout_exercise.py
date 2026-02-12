from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import WorkoutExercise
from src.repos.alchemy import BaseRepo

__all__ = ["WorkoutExerciseRepo"]


class WorkoutExerciseRepo(BaseRepo[WorkoutExercise]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=WorkoutExercise)
