from fastapi import APIRouter

from .auth import auth
from .account import account
from .exercise import exercise
from .workout import workout

__all__ = ["v1"]

v1 = APIRouter(prefix="/v1")
v1.include_router(router=auth)
v1.include_router(router=account)
v1.include_router(router=exercise)
v1.include_router(router=workout)
