from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from src.types.annotated import PasswordStr
from src.types.base import ImmutableDTO

__all__ = ["AccountDetailResponseDTO"]


class AccountDetailResponseDTO(ImmutableDTO):
    id: UUID
    email: EmailStr
    password: PasswordStr

    username: str

    created_at: datetime
    updated_at: datetime | None
