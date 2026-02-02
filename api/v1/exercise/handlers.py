from fastapi import APIRouter, Depends
from starlette import status

from api.annotated_types import PageQuery, PageSizeQuery, ExerciseID
from api.dependencies.services import AuthenticateHeaderDepends, ExerciseServiceDepends
from src.types import ExerciseCreateRequestDTO, ExerciseFilterDTO, Paginator, ExerciseDetailResponseDTO

router = APIRouter(tags=["Exercise"], dependencies=[AuthenticateHeaderDepends])


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=Paginator[ExerciseDetailResponseDTO],
)
async def exercise_list(
        service: ExerciseServiceDepends,
        filters: ExerciseFilterDTO = Depends(),
        page: PageQuery = 1,
        page_size: PageSizeQuery = 10
):
    return await service.list(page=page, page_size=page_size, filters=filters)


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
)
async def get_exercise(service: ExerciseServiceDepends, exercise_id: ExerciseID):
    return await service.get(exercise_id=exercise_id)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
)
async def create_exercise(service: ExerciseServiceDepends, data: ExerciseCreateRequestDTO):
    return await service.post(data=data)


@router.patch(
    path="/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_exercise(
        service: ExerciseServiceDepends,
):
    pass


@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_exercise(
        service: ExerciseServiceDepends,
):
    pass
