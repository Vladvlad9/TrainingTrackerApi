from typing import Annotated

from fastapi import Path
from pydantic import UUID4


AccountID = Annotated[
    UUID4,
    Path(
        title="Account ID",
        description="<p>Account unique identifier</p>",
        alias="id",
    ),
]