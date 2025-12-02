from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import Account
from src.repos.alchemy.base import BaseRepo

__all__ = ["AccountRepo"]


class AccountRepo(BaseRepo[Account]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=Account)
