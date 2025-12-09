from typing import Annotated

from fastapi import Depends

from api.dependencies.database_session import DBSession
from api.services.exercise import RESTExerciseService

__all__ = ["ExerciseServiceDepends"]


async def _exercise_service(session: DBSession) -> RESTExerciseService:
    return RESTExerciseService(session=session)


ExerciseServiceDepends = Annotated[RESTExerciseService, Depends(dependency=_exercise_service)]
