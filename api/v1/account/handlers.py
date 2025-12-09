from fastapi import APIRouter
from starlette import status
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_429_TOO_MANY_REQUESTS

from api.annotated_types import AccountID
from api.dependencies.services import AccountServiceDepends, AuthenticateHeaderDepends, CurrentUserIDDeps
from src.types.account import AccountDetailResponseDTO, AccountUpdateRequestDTO
from src.types.exeptions import HTTPExceptionErrorDTO, ToManyRequestsErrorDTO

router = APIRouter(tags=["Account"], dependencies=[AuthenticateHeaderDepends])


@router.get(
    path="/",
    response_model=AccountDetailResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def detail_me(service: AccountServiceDepends, current_user_id: CurrentUserIDDeps) -> AccountDetailResponseDTO:
    return await service.get(account_id=current_user_id)


@router.get(
    path="/{id}",
    response_model=AccountDetailResponseDTO,
    status_code=status.HTTP_200_OK,
)
async def detail_account(service: AccountServiceDepends, account_id: AccountID):
    return await service.get(account_id=account_id)

@router.patch(
    path="/{id}",
    response_model=AccountDetailResponseDTO,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPExceptionErrorDTO},
        HTTP_429_TOO_MANY_REQUESTS: {"model": ToManyRequestsErrorDTO},
    },
)
async def update_account(service: AccountServiceDepends, data: AccountUpdateRequestDTO, account_id: AccountID):
    return await service.path(account_id=account_id, data=data)
