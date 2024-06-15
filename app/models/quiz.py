import uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base, db_session

from sqlalchemy import select


class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True)
    id_photo: Mapped[str] = mapped_column(nullable=False)
    id_mark: Mapped[str] = mapped_column(nullable=False)
    label: Mapped[int] = mapped_column(nullable=True)

    @classmethod
    async def get_quiz(cls):
        return await db_session.get().execute(select(Quiz))
