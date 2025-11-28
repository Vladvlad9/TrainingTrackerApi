from fastapi import APIRouter
from starlette import status

from src.types.exeptions import ToManyRequestsErrorDTO, HTTPExceptionErrorDTO

router = APIRouter(tags=["Auth"])

@router.post(
    path="/signup",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up",
    responses={
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ToManyRequestsErrorDTO},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
    }

)
async def sign_up():
    return {"test": "test"}