__all__ = [
    "JWTError",
    "DecodeError",
    "JWTStorageUnavailableError",
    "IncorrectJWTBanPayloadError",
]


class JWTError(Exception):
    detail: str = "jwt_error"


class DecodeError(JWTError):
    detail: str = "jwt_decode"


class JWTStorageUnavailableError(JWTError):
    detail: str = "jwt_storage_unavailable"


class IncorrectJWTBanPayloadError(JWTError):
    detail: str = "incorrect_jwt_ban_payload"