from abc import ABC
from typing import TypeVar, Generic, Any

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)

class BaseRepo(ABC, Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: type[ModelType]):
        self._session = session
        self._model = model

    async def get(self, filters: list[Any], options: list[Any] | None = None) -> ModelType:
        statement = select(self._model).filter(*filters)
        if options:
            statement = statement.options(*options)

        return await self._session.scalar(statement)

    async def insert(self, obj: dict) -> ModelType:
        result = await self._session.execute(
            statement=insert(self._model).values(**obj).returning(self._model)
        )
        await self._session.commit()
        return result.scalar_one_or_none()

    async def update(self, filters: list[Any], obj: dict) -> ModelType:
        statement = update(self._model).filter(*filters).values(**obj).returning(self._model)
        result = await self._session.execute(statement)
        await self._session.commit()
        return result.scalar_one_or_none()

    async def delete(self, filters: list[Any]) -> ModelType:
        statement = delete(self._model).filter(*filters).returning(self._model)
        result = await self._session.execute(statement)
        await self._session.commit()
        return result.scalar_one_or_none()

