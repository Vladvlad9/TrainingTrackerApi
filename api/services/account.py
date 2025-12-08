from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.services.account import AccountService
from src.types.account import AccountResponseIdDTO, AccountDetailResponseDTO, AccountUpdateRequestDTO

__all__ = ["RESTAccountService"]


class RESTAccountService:
    def __init__(self, session: AsyncSession):
        self._account_service = AccountService(session=session)

    async def get(self, account_id: UUID) -> AccountDetailResponseDTO:
        return await self._account_service.get(account_id=account_id)

    async def path(self, account_id: UUID, data: AccountUpdateRequestDTO):
        return await self._account_service.path(account_id=account_id, data=data)
