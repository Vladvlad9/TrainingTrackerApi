from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import Workout
from src.repos.alchemy import BaseRepo

__all__ = ["WorkoutRepo"]


class WorkoutRepo(BaseRepo[Workout]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=Workout)
