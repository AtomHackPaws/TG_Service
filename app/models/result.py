from typing import Optional
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import JSONB, insert

from app.db.base import Base
from app.db import db_session


class Result(Base):
    __tablename__ = "result"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    result: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    profile_id = mapped_column(
        BigInteger(),
        ForeignKey("profile.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    profile = relationship("Profile", back_populates="results", passive_deletes=True)

    @classmethod
    async def create_result(cls, result, profile_id):
        stmt = (
            insert(Result)
            .values(result=result, profile_id=profile_id)
            .returning(Result.id)
        )
        return await db_session.get().execute(stmt)
