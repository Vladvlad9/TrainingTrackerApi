from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from api.exception_handlers.factory import ExceptionHandlerFactory
from api.exceptions import ObjectExistsException, ObjectNotFoundException, InternalServerException
from src.exceptions import ObjectAlreadyExistError, ObjectNotFoundError
from src.services.workout import WorkoutService

__all__ = ["RESTWorkoutService"]

from src.types import WorkoutCreateDTO

workout_exception_handler = ExceptionHandlerFactory(
    exc_mapping={
        ObjectAlreadyExistError: ObjectExistsException(name="workout"),
        ObjectNotFoundError: ObjectNotFoundException(name="workout"),
    },
    default_exc=InternalServerException(name="Workout"),
)


class RESTWorkoutService:
    def __init__(self, session: AsyncSession):
        self._workout_service = WorkoutService(session=session)

    async def list(self):
        return await self._workout_service.list()

    @workout_exception_handler()
    async def get(self):
        return await self._workout_service.get()

    @workout_exception_handler()
    async def create(self, workouts: WorkoutCreateDTO):
        return await self._workout_service.post(data=workouts)

    @workout_exception_handler()
    async def update(self):
        return await self._workout_service.patch()

    @workout_exception_handler()
    async def delete(self, workout_id: UUID4):
        return await self._workout_service.delete(workout_id=workout_id)
