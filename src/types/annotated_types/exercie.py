from typing import Annotated

from pydantic import Field

__all__ = ["NameStr", "DescriptionStr"]

NameStr = Annotated[
    str,
    Field(
        title="Exercise Name",
        description="Название упражнения (2-100 символов)",
        examples=["Жим штанги лежа", "Приседания со штангой", "Подтягивания"],
        min_length=3,
        max_length=200,
    )
]

DescriptionStr = Annotated[
    str,
    Field(
        title="Exercise Description",
        description="",
        examples=["Жим штанги лежа", "Приседания со штангой", "Подтягивания"],
        min_length=3,
        max_length=200,
    )
]
