from fastapi import APIRouter

from .handlers import router

__all__ = ['auth']

auth = APIRouter(prefix="/auth")
auth.include_router(router=router)
