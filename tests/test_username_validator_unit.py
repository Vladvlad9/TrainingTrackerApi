import pytest

from src.types.validators.username import validate_username


def test_validate_username_returns_value_for_valid_identifier() -> None:
    value = "_user_123"
    assert validate_username(value) == value


def test_validate_username_raises_value_error_for_invalid_identifier() -> None:
    with pytest.raises(ValueError):
        validate_username("bad-user")
