from uuid import uuid4

from sqlalchemy import UUID, VARCHAR, CheckConstraint, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.databse.alchemy.mixins import LifecycleMixin
from src.databse.alchemy.models.base import Base

from src.enums import ExerciseCategory, ExerciseMuscleGroups

__all__ = ["Exercise"]


class Exercise(Base, LifecycleMixin):
    __table_args__ = (
        CheckConstraint(sqltext="length(name) >= 3", name="name_exercise_min_length"),
        CheckConstraint(sqltext="length(description) >= 5", name="description_exercise_min_length"),
    )
    id: Mapped[UUID] = mapped_column(
        UUID,
        insert_default=uuid4,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    description: Mapped[str] = mapped_column(VARCHAR(200), unique=True, nullable=True)
    category: Mapped[ExerciseCategory | None] = mapped_column(Enum(ExerciseCategory), nullable=True)
    muscle_group: Mapped[ExerciseMuscleGroups | None] = mapped_column(Enum(ExerciseMuscleGroups), nullable=True)

    exercises = relationship(
        argument="Exercise",
        secondary="workout_exercises",
        back_populates="workouts"
    )

    def __repr__(self) -> str:
        return (f"<Exercise(id={self.id}, "
                f"name='{self.name}', "
                f"category='{self.category}', "
                f"muscle_group='{self.muscle_group}')>"
                f"")

    def __str__(self) -> str:
        return f"Exercise: {self.name}"
