from fastapi import APIRouter
from starlette import status

from api.dependencies.services.auth import AuthServiceDepends
from src.types.auth.sign_up import SignUpRequestDTO
from src.types.auth.sing_in import SignInRequestDTO
from src.types.exeptions import (
    ToManyRequestsErrorDTO,
    HTTPExceptionErrorDTO,
    IncorrectPasswordErrorDTO
)

router = APIRouter(tags=["Auth"])


@router.post(
    path="/signup",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="Регистрация",
    responses={
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ToManyRequestsErrorDTO},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
    }
)
async def sign_up(data: SignUpRequestDTO, service: AuthServiceDepends):
    return service.sign_up(data=data)


@router.post(
    path="/signin",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="Вход",
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": IncorrectPasswordErrorDTO},
        # HTTP_404_NOT_FOUND: {"model": ObjectNotFoundErrorDTO(name="user")},
        status.HTTP_429_TOO_MANY_REQUESTS: {"model": ToManyRequestsErrorDTO},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
    },
)
async def sign_in(data: SignInRequestDTO, service: AuthServiceDepends):
    return await service.sign_in(data=data)
