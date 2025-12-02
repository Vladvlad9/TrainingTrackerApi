from sqlalchemy.ext.asyncio import AsyncSession

from src.services import AuthService
from src.types import SignInRequestDTO, SignUpRequestDTO, TokenPairDTO

__all__ = ["RESTAuthService"]


class RESTAuthService:
    def __init__(self, session: AsyncSession):
        self._auth_service = AuthService(session=session)

    async def sign_in(self, data: SignInRequestDTO) -> TokenPairDTO:
        return await self._auth_service.sign_in(data=data)

    async def sign_up(self, data: SignUpRequestDTO):
        return await self._auth_service.sign_up(data=data)
