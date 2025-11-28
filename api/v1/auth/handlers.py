from fastapi import APIRouter
from starlette import status

router = APIRouter(tags=["Auth"])

@router.post(
    path="/signup",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up",
    tags=["Sign up"],

)
async def sign_up():
    return {"test": "test"}