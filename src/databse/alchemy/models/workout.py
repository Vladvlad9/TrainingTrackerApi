import datetime
import uuid

from sqlalchemy import UUID, CheckConstraint, VARCHAR, TIMESTAMP, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.databse.alchemy.mixins import LifecycleMixin
from src.databse.alchemy.models.base import Base

from src.enums import WorkoutEnum

__all__ = ["Workout"]


class Workout(Base, LifecycleMixin):
    __table_args__ = (
        CheckConstraint(sqltext="length(title) >= 3", name="title_workout_min_length"),
        CheckConstraint(sqltext="note IS NULL OR length(note) >= 5", name="note_workout_min_length"),
    )

    id: Mapped[UUID] = mapped_column(
        UUID,
        insert_default=uuid.uuid4,
        primary_key=True,
    )

    title: Mapped[str] = mapped_column(
        VARCHAR(15),
        nullable=False,
        unique=True,
    )
    note: Mapped[str | None] = mapped_column(VARCHAR(100), nullable=True)
    scheduled_at: Mapped[datetime.datetime | None] = mapped_column(TIMESTAMP(timezone=True))
    status: Mapped[WorkoutEnum | None] = mapped_column(Enum(WorkoutEnum), nullable=True)

    account = relationship(argument="Account", back_populates="workouts")

    workout_exercises = relationship(
        argument="WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Workout(id={self.id}, title='{self.title}', status='{self.status}')>"

    def __str__(self):
        scheduled_date = self.scheduled_at.date() if self.scheduled_at else ""
        return f'{self.title or "Тренировка"} - {scheduled_date}'
