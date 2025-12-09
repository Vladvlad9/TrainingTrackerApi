from typing import Annotated

from pydantic import AfterValidator, Field

from src.types.validators import validate_email

__all__ = ["ConEmailStr"]

ConEmailStr = Annotated[
    str,
    AfterValidator(func=validate_email),
    Field(
        title="Account Email Address",
        examples=["user@example.com"],
    ),
]
