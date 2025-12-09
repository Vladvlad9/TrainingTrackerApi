__all__ = ["validate_username"]


def validate_username(value: str) -> str:
    if not value.isidentifier():
        raise ValueError(
            "username can consist only of letters, numbers and underscores, starting with a letter or an underscore"
        )
    return value
