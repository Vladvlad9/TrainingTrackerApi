from typing import Annotated

from fastapi import Depends

from api.dependencies.database_session import DBSession
from api.services.auth import RESTAuthService


async def _get_auth_service(session: DBSession) -> RESTAuthService:
    return RESTAuthService(session=session)

AuthServiceDepends = Annotated[RESTAuthService, Depends(dependency=_get_auth_service)]