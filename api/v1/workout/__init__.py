from fastapi import APIRouter

from .handlers import router

workout = APIRouter(prefix="/workout")
workout.include_router(router)
