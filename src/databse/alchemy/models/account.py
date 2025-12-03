from uuid import uuid4

from sqlalchemy import CheckConstraint, String, UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.databse.alchemy.mixins import LifecycleMixin
from src.databse.alchemy.models.base import Base

__all__ = ["Account"]

class Account(Base, LifecycleMixin):
    __table_args__ = (
        CheckConstraint(sqltext="length(email) >= 5", name="email_min_length"),
        CheckConstraint(sqltext="email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'", name="email_format"),
        CheckConstraint(sqltext="length(username) >= 2", name="username_min_length"),
    )
    id: Mapped[UUID] = mapped_column(
        UUID,
        insert_default=uuid4,
        primary_key=True,
    )

    email: Mapped[str] = mapped_column(String(254), unique=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=True)

    username: Mapped[str] = mapped_column(VARCHAR(50), server_default=f"User_{str(uuid4())}", unique=True)

    def __str__(self) -> str:
        return f"Account {self.email}"
