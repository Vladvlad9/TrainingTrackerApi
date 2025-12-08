from fastapi import APIRouter
from starlette import status

from api.annotated_types import AccountID
from api.dependencies.services.account import AccountServiceDepends
from api.dependencies.services.auth import AuthenticateHeaderDeps, CurrentUserIDDeps
from src.types.account import AccountDetailResponseDTO, AccountUpdateRequestDTO

router = APIRouter(tags=["Account"], dependencies=[AuthenticateHeaderDeps])


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
)
async def update_account(service: AccountServiceDepends, data: AccountUpdateRequestDTO, account_id: AccountID):
    return await service.path(account_id=account_id, data=data)
