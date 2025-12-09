from enum import StrEnum, unique, auto

__all__ = ['WorkoutEnum']


@unique
class WorkoutEnum(StrEnum):
    PLANNED = auto()
    COMPLETED = auto()
