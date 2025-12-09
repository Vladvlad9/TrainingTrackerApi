from typing import Annotated

from fastapi import Path
from pydantic import UUID4

__all__ = ["ExerciseID"]

ExerciseID = Annotated[
    UUID4,
    Path(
        title="Exercise ID",
        description="<p>Exercise unique identifier</p>",
        alias="id",
    ),
]
