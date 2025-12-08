from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from src.types.base import ImmutableDTO

__all__ = ["AccountDetailResponseDTO", "AccountResponseIdDTO", "AccountUpdateRequestDTO"]


class AccountResponseIdDTO(ImmutableDTO):
    id: UUID


class AccountUpdateRequestDTO(ImmutableDTO):
    username: str
    email: EmailStr


class AccountDetailResponseDTO(ImmutableDTO):
    id: UUID
    email: EmailStr
    # password_hash: PasswordStr = Field(alias="password")

    username: str

    created_at: datetime
    update_at: datetime | None
