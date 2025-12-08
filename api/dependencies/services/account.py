from typing import Annotated

from fastapi import Depends

from api.dependencies.database_session import DBSession
from api.services.account import RESTAccountService

__all__ = ["AccountServiceDepends"]


async def _account_service(session: DBSession) -> RESTAccountService:
    return RESTAccountService(session=session)


AccountServiceDepends = Annotated[RESTAccountService, Depends(dependency=_account_service)]
