from typing import Annotated

from fastapi import Path
from pydantic import UUID4

__all__ = ["WorkoutID"]

WorkoutID = Annotated[
    UUID4,
    Path(
        title="WorkoutID ID",
        description="<p>WorkoutID unique identifier</p>",
        alias="id",
    ),
]
