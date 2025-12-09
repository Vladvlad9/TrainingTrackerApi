from typing import Annotated

from fastapi import Depends

from api.dependencies.database_session import DBSession

__all__ = ["WorkoutServiceDepends"]


async def _workout_service(session: DBSession):
    pass


WorkoutServiceDepends = Annotated[..., Depends(dependency=_workout_service)]
