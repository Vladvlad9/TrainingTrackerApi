import os
import sys
from typing import Any

import pytest
from fastapi.testclient import TestClient


def _set_test_env() -> None:
    os.environ.setdefault("DATABASE_POSTGRES_DSN", "postgresql+asyncpg://user:pass@localhost:5432/test")
    os.environ.setdefault("REDIS_DSN", "redis://localhost:6379/0")
    os.environ.setdefault("SERVER_HOST", "127.0.0.1")
    os.environ.setdefault("SERVER_PORT", "8000")
    os.environ.setdefault("APP_ENV", "test")

    os.environ.setdefault("JWT_ACCESS_SECRET_KEY", "test_access_secret")
    os.environ.setdefault("JWT_REFRESH_SECRET_KEY", "test_refresh_secret")
    os.environ.setdefault("JWT_ACCESS_PUBLIC_KEY", "test_access_public")
    os.environ.setdefault("JWT_REFRESH_PUBLIC_KEY", "test_refresh_public")
    os.environ.setdefault("JWT_ACCESS_EXP_TIME", "15")
    os.environ.setdefault("JWT_REFRESH_EXP_TIME", "60")
    os.environ.setdefault("JWT_ACCESS_ALGORITHM", "HS256")
    os.environ.setdefault("JWT_REFRESH_ALGORITHM", "HS256")


@pytest.fixture()
def client() -> TestClient:
    _set_test_env()

    # Ensure settings pick up our env if the module was imported elsewhere.
    for module_name in ["settings", "settings.settings"]:
        if module_name in sys.modules:
            del sys.modules[module_name]

    from app.app import get_application
    from api.dependencies.services.auth import _get_auth_service

    class DummyAuthService:
        async def sign_up(self, data: Any) -> None:
            return None

        async def sign_in(self, data: Any) -> dict[str, str]:
            return {
                "access_token": "access-token",
                "refresh_token": "refresh-token",
            }

    async def override_auth_service() -> DummyAuthService:
        return DummyAuthService()

    app = get_application()
    app.dependency_overrides[_get_auth_service] = override_auth_service

    return TestClient(app)


def test_auth_signup(client: TestClient) -> None:
    response = client.post(
        "/api/v1/auth/signup",
        json={"email": "user@example.com", "password": "StrongPass1!"},
    )

    assert response.status_code == 201


def test_auth_signin(client: TestClient) -> None:
    response = client.post(
        "/api/v1/auth/signin",
        json={"email": "user@example.com", "password": "StrongPass1!"},
    )

    assert response.status_code == 201
    assert response.json() == {
        "access_token": "access-token",
        "refresh_token": "refresh-token",
    }
