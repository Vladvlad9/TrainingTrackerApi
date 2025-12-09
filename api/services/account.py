from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.exception_handlers.factory import ExceptionHandlerFactory
from api.exceptions import ObjectNotFoundException, InternalServerException
from src.exceptions import ObjectNotFoundError
from src.services.account import AccountService
from src.types.account import AccountDetailResponseDTO, AccountUpdateRequestDTO

__all__ = ["RESTAccountService"]

account_exception_handler = ExceptionHandlerFactory(
    exc_mapping={
        ObjectNotFoundError: ObjectNotFoundException(name="account"),
    },
    default_exc=InternalServerException(name="Exercise"),
)


class RESTAccountService:
    def __init__(self, session: AsyncSession):
        self._account_service = AccountService(session=session)

    @account_exception_handler()
    async def get(self, account_id: UUID) -> AccountDetailResponseDTO:
        return await self._account_service.get(account_id=account_id)

    @account_exception_handler()
    async def path(self, account_id: UUID, data: AccountUpdateRequestDTO):
        return await self._account_service.path(account_id=account_id, data=data)
