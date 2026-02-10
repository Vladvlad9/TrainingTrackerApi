from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from src.repos.alchemy import WorkoutRepo

__all__ = ["WorkoutService"]


class WorkoutService:
    def __init__(self, session: AsyncSession):
        self._workout_repo = WorkoutRepo(session=session)

    async def get(self):
        pass

    async def post(self):
        pass

    async def patch(self):
        pass

    async def delete(self, workout_id: UUID4):
        pass

    async def list(self):
        pass
