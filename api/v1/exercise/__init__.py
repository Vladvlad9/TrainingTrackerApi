from fastapi import APIRouter

from .handlers import router

exercise = APIRouter(prefix="/exercise")
exercise.include_router(router)