from typing import Optional
import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base import Base


class Result(Base):
    __tablename__ = "result"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True)
    result: Mapped[Optional[dict]] = mapped_column(JSONB)
    profile_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("profile.id", ondelete="CASCADE"), nullable=False, index=True
    )

    profile = relationship("Profile", back_populates="results", passive_deletes=True)
