import uuid
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey

from app.db.base import Base

from datetime import datetime


class Profile(Base):
    __tablename__ = "profile"

    id = mapped_column(BigInteger(), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sa.func.now()
    )
    check_community: Mapped[bool] = mapped_column(nullable=False, default=False)
    master_link: Mapped[uuid.UUID]
    community_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("community.id", ondelete="CASCADE"), nullable=False, index=True
    )

    results = relationship("Result", back_populates="profile", cascade="all, delete")
    community = relationship(
        "Community", back_populates="profiles", passive_deletes=True
    )
