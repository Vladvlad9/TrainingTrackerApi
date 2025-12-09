from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from api.exception_handlers.factory import ExceptionHandlerFactory
from api.exceptions import (
    IncorrectPasswordException,
    ServiceResponseValidationException,
    ObjectNotFoundException,
    ObjectExistsException,
    InternalServerException
)
from src.exceptions import ObjectNotFoundError, IncorrectPasswordError, ObjectAlreadyExistError
from src.services import AuthService
from src.types import SignInRequestDTO, SignUpRequestDTO, TokenPairDTO

__all__ = ["RESTAuthService"]

auth_exception_handler = ExceptionHandlerFactory(
    exc_mapping={
        ValidationError: ServiceResponseValidationException(name="auth"),
        ObjectNotFoundError: ObjectNotFoundException(name="account"),
        IncorrectPasswordError: IncorrectPasswordException,
        ObjectAlreadyExistError: ObjectExistsException(name="account"),
    },
    default_exc=InternalServerException(name="account"),
)

class RESTAuthService:
    def __init__(self, session: AsyncSession):
        self._auth_service = AuthService(session=session)

    @auth_exception_handler()
    async def sign_in(self, data: SignInRequestDTO) -> TokenPairDTO:
        return await self._auth_service.sign_in(data=data)

    @auth_exception_handler()
    async def sign_up(self, data: SignUpRequestDTO):
        return await self._auth_service.sign_up(data=data)