from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.databse.alchemy.models import Account
from src.exceptions import ObjectNotFoundError
from src.repos.alchemy import AccountRepo
from src.types.account import AccountDetailResponseDTO, AccountUpdateRequestDTO

__all__ = ["AccountService"]


class AccountService:
    def __init__(self, session: AsyncSession):
        self._repo = AccountRepo(session=session)

    async def get(self, account_id: UUID) -> AccountDetailResponseDTO:
        account = await self._repo.get(filters=[Account.id == account_id])
        if not account:
            raise ObjectNotFoundError(name="account")

        return AccountDetailResponseDTO.model_validate(obj=account, from_attributes=True)

    async def path(self, account_id: UUID, data: AccountUpdateRequestDTO) -> Account:
        account = data.model_dump(exclude_unset=True)

        return await self._repo.update(obj=account, filters=[Account.id == account_id])
