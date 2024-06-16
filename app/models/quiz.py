import uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base, db_session
from sqlalchemy import select, func


class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    id_photo: Mapped[str] = mapped_column(nullable=False)
    id_mark: Mapped[str] = mapped_column(nullable=False)
    label: Mapped[int] = mapped_column(nullable=True)

    @classmethod
    async def get_all_quiz(cls):
        return await db_session.get().execute(select(Quiz))

    @classmethod
    async def get_random_select(cls):
        result = await db_session.get().execute(select(Quiz).order_by(func.random()))
        return result.scalars().first()

    @classmethod
    async def get_quiz_by_id(cls, id: uuid):
        result = await db_session.get().execute(select(Quiz).where(Quiz.id == id))
        return result.scalars().first()
