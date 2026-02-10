from typing import Annotated

from fastapi import Depends

from api.dependencies.database_session import DBSession

from api.services.workout import RESTWorkoutService

__all__ = ["WorkoutServiceDepends"]


async def _workout_service(session: DBSession) -> RESTWorkoutService:
    return RESTWorkoutService(session=session)


WorkoutServiceDepends = Annotated[RESTWorkoutService, Depends(dependency=_workout_service)]
