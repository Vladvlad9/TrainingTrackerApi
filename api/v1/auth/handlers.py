from fastapi import APIRouter

router = APIRouter(tags=["Auth"])

@router.get("/")
async def test():
    return {"test": "test"}