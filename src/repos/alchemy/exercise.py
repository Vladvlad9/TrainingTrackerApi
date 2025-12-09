from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import Exercise
from src.repos.alchemy import BaseRepo

__all__ = ['ExerciseRepo']


class ExerciseRepo(BaseRepo[Exercise]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=Exercise)
