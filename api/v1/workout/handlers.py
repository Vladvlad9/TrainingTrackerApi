from fastapi import APIRouter
from starlette import status

from api.annotated_types import WorkoutID
from api.dependencies.services import WorkoutServiceDepends
from src.types import WorkoutExerciseDTO, WorkoutCreateDTO, WorkoutBaseDTO

router = APIRouter(tags=["Workout"])


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=WorkoutBaseDTO
)
async def list_workouts(service: WorkoutServiceDepends):
    pass


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
)
async def create_workout(workouts: WorkoutCreateDTO, service: WorkoutServiceDepends):
    return await service.create(workouts=workouts)


@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK
)
async def get_workouts(workout_id: WorkoutID, service: WorkoutServiceDepends):
    return await service.get()


@router.patch(
    path="/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_workout(workout_id: WorkoutID, service: WorkoutServiceDepends):
    return await service.update()


@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_workout(workout_id: WorkoutID, service: WorkoutServiceDepends):
    return await service.delete(workout_id=workout_id)
