from sqlalchemy.ext.asyncio import AsyncSession

from src.types import SignInRequestDTO, SignUpRequestDTO, TokenPairDTO


class AuthService:
    def __init__(self, session: AsyncSession):
        pass

    async def sign_in(self, data: SignInRequestDTO) -> TokenPairDTO:
        pass

    async def sign_up(self, data: SignUpRequestDTO):
        pass
