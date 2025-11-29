from typing import Annotated
from uuid import UUID

from fastapi import Security, Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

from api.dependencies.database_session import DBSession
from api.exceptions import TokenNotProvidedException, InvalidTokenOrExpiredException
from src.types.auth.token import TokenPayload
from src.utils.jwt import DecodeError
from src.utils.jwt.manager import JWTManager


async def _authenticate(
        creds: Annotated[HTTPAuthorizationCredentials, Security(dependency=HTTPBearer(auto_error=False))],
) -> HTTPAuthorizationCredentials:
    if creds is None:
        raise TokenNotProvidedException()
    return creds


HTTPAuthorizationCredentialsDepends = Annotated[HTTPAuthorizationCredentials, Security(dependency=_authenticate)]


async def _get_token_payload(credentials: HTTPAuthorizationCredentialsDepends) -> TokenPayload:
    try:
        return await JWTManager.decode_access_token(token=credentials.credentials)
    except DecodeError:
        raise InvalidTokenOrExpiredException()


TokenPayloadDepends = Annotated[TokenPayload, Depends(dependency=_get_token_payload)]


async def _get_auth_service(session: DBSession) -> RESTAuthService:
    return RESTAuthService(session=session)


AuthServiceDepends = Annotated[RESTAuthService, Depends(dependency=_get_auth_service)]


async def _current_user_id(token_payload: TokenPayloadDepends):
    if token_payload.get("sub"):
        return token_payload.get("sub")
    return None


CurrentUserIDDeps = Annotated[UUID, Depends(dependency=_current_user_id)]

AuthenticateHeaderDeps = Depends(dependency=_authenticate)
