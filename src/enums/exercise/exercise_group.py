from enum import StrEnum, unique, auto

__all__ = ["ExerciseMuscleGroups"]


@unique
class ExerciseMuscleGroups(StrEnum):
    BACK = auto()
    CHEST = auto()
    ARMS = auto()
    LEGS = auto()
    SHOULDERS = auto()
