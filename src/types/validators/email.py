from email_validator import EmailNotValidError
from pydantic import validate_email as validate_email_pydantic


__all__ = ["validate_email"]


def validate_email(value: str) -> str:
    value = value.lower()
    if len(value) > 254:
        raise ValueError("A fan of long names! Alas, emails can’t be longer than 254 characters.")
    if len(value) < 6:
        raise ValueError("It’s true that less is more. But an email can’t be shorter than 6 characters.")
    if len(value.split("@")[0]) > 63:
        raise ValueError("Email should have not more than 63 characters before domain.")
    try:
        validate_email_pydantic(value)
    except EmailNotValidError as exc:
        raise ValueError("Make sure the email follows this format: `email@example.com`") from exc
    return value
