from datetime import datetime
from typing import Annotated

from pydantic import Field

__all__ = [
    "SetsTypes",
    "RepsTypes",
    "WeightTypes",
    "DurationMinutesTypes",

    "WorkoutTitleTypes",
    "WorkoutNoteTypes",
    "WorkoutScheduledAtTypes",
    "WorkoutStatusTypes",
]

from src.enums import WorkoutEnum

SetsTypes = Annotated[
    int | None,
    Field(
        default=None,
        title="...",
        description="Количество подходов",
        examples=["1"],
        ge=1,
        le=20
    )
]

RepsTypes = Annotated[
    int | None,
    Field(
        default=None,
        title="Количество повторений",
        description="Количество повторений",
        examples=["1"],
        ge=1,
        le=100
    )
]

WeightTypes = Annotated[
    int | None,
    Field(
        default=None,
        title="...",
        description="Вес (кг)",
        examples=[1],
        ge=0,
        le=500
    )
]

DurationMinutesTypes = Annotated[
    int | None,
    Field(
        default=None,
        title="...",
        description="Длительность в минутах",
        examples=[1],
        ge=0,
        le=300
    )
]

WorkoutTitleTypes = Annotated[
    str,
    Field(
        ...,
        title="Название тренировки",
        description="Название тренировки",
        examples=["Грудь и бицепс"],
        min_length=3,
        max_length=15
    )
]

WorkoutNoteTypes = Annotated[
    int | None,
    Field(
        default=None,
        title="Заметка",
        description="Заметка",
        examples=["string"],
        min_length=5,
        max_length=100
    )
]

WorkoutScheduledAtTypes = Annotated[
    datetime | None,
    Field(
        default=None,
        title="Дата и время тренировки",
        description="Дата и время тренировки"
    )
]


WorkoutStatusTypes = Annotated[
    WorkoutEnum | None,
    Field(
        default=None,
        title="Статус тренировки",
        description="Статус тренировки",
    )
]
