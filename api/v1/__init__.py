from fastapi import APIRouter

from .auth import auth
from .account import account

__all__ = ["v1"]

v1 = APIRouter(prefix="/v1")
v1.include_router(router=auth)
v1.include_router(router=account)
