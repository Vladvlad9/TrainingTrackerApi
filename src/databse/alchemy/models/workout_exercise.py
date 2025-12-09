import uuid
from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, SmallInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.databse.alchemy.mixins import LifecycleMixin
from src.databse.alchemy.models.base import Base

__all__ = ["WorkoutExercise"]

if TYPE_CHECKING:
    from .workout import Workout
    from .exercise import Exercise


class WorkoutExercise(Base, LifecycleMixin):
    id: Mapped[UUID] = mapped_column(
        UUID,
        insert_default=uuid.uuid4,
        primary_key=True,
    )

    workout_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey('workout.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )

    exercise_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey('exercise.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )

    sets: Mapped[int | None] = mapped_column(SmallInteger, nullable=True, default=3)
    reps: Mapped[int | None] = mapped_column(SmallInteger, nullable=True, default=10)
    weight: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    workout: Mapped["Workout"] = relationship(argument="Workout", back_populates="workout_exercises")
    exercise: Mapped["Exercise"] = relationship(argument="Exercise", back_populates="workout_exercises")

    def __repr__(self) -> str:
        return f"<WorkoutExercise(id={self.id}, workout_id={self.workout_id}, exercise_id={self.exercise_id})>"

    def __str__(self) -> str:
        return f"WorkoutExercise(id={self.id}, exercise_id={self.exercise_id})"
