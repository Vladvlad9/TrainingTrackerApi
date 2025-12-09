from enum import Enum
from typing import Annotated, Literal, Optional
from uuid import UUID

from pydantic import Field, field_serializer

from src.enums import ExerciseCategory, ExerciseMuscleGroups
from src.types.annotated_types import NameStr, DescriptionStr
from src.types.base import ImmutableDTO

__all__ = ["ExerciseCreateRequestDTO", "ExerciseFilterDTO", "ExerciseDetailResponseDTO"]


class ExerciseBaseDTO(ImmutableDTO):
    name: NameStr
    description: DescriptionStr
    category: ExerciseCategory
    muscle_group: ExerciseMuscleGroups


class ExerciseFilterDTO(ImmutableDTO):
    q: Annotated[str | None, Field()] = None
    # sort_by: Literal["id"] = Field(default="id")
    # sort: Literal["asc", "desc"] = Field(default="asc")
    category: ExerciseCategory | None = Field(default=None)
    muscle_group: ExerciseMuscleGroups | None = Field(default=None)


class ExerciseDetailResponseDTO(ExerciseBaseDTO):
    id: UUID


class ExerciseCreateRequestDTO(ExerciseBaseDTO):
    pass
