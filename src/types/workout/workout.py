from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import Field, field_validator, ConfigDict

from src.enums import WorkoutEnum
from src.types.annotated_types import (
    SetsTypes,
    RepsTypes,
    WeightTypes,
    DurationMinutesTypes,
    WorkoutTitleTypes,
    WorkoutNoteTypes,
    WorkoutScheduledAtTypes,
    WorkoutStatusTypes
)
from src.types.base import ImmutableDTO

__all__ = ["WorkoutExerciseDTO", "WorkoutCreateDTO", "WorkoutBaseDTO"]


class WorkoutDTO(ImmutableDTO):
    title: WorkoutTitleTypes
    note: WorkoutNoteTypes
    scheduled_at: WorkoutScheduledAtTypes
    status: WorkoutStatusTypes


class WorkoutExerciseDTO(ImmutableDTO):
    exercise_id: UUID
    sets: SetsTypes
    reps: RepsTypes
    weight: WeightTypes
    duration_minutes: DurationMinutesTypes


class WorkoutCreateDTO(ImmutableDTO):
    title: WorkoutTitleTypes
    note: WorkoutNoteTypes
    scheduled_at: WorkoutScheduledAtTypes
    status: WorkoutStatusTypes
    exercises: List[WorkoutExerciseDTO]


class WorkoutBaseDTO(WorkoutCreateDTO):
    id: UUID
