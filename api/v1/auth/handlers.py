from fastapi import APIRouter

router = APIRouter(tags=["Auth"])

@router.get("/")
async def tests():
    return {"test": "test"}