from typing import Optional
import uuid
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import insert

from app.db import Base, db_session

from datetime import datetime


class Profile(Base):
    __tablename__ = "profile"

    id = mapped_column(BigInteger(), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sa.func.now()
    )
    master_link: Mapped[Optional[uuid.UUID]] = mapped_column(nullable=True)

    results = relationship("Result", back_populates="profile", cascade="all, delete")

    @classmethod
    async def create_user(cls, id, username):
        stmt = insert(Profile).values(id=id, username=username)
        stmt = stmt.on_conflict_do_nothing(index_elements=["id"])
        await db_session.get().execute(stmt)
