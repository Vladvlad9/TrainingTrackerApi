from enum import StrEnum, unique, auto

__all__ = ["ExerciseCategory"]


@unique
class ExerciseCategory(StrEnum):
    CARDIO = auto()
    STRENGTH = auto()
    STRETCH = auto()
