import uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Community(Base):
    __tablename__ = "community"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True)
    community_name: Mapped[str] = mapped_column()

    profiles = relationship(
        "Community", back_populates="community", cascade="all, delete"
    )
