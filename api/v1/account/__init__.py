from fastapi import APIRouter
from .handlers import router

__all__ = ["account"]

account = APIRouter(prefix="/account")
account.include_router(router)
