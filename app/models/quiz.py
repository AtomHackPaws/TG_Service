import uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    id_photo: Mapped[str] = mapped_column(nullable=False)
    id_mark: Mapped[str] = mapped_column(nullable=False)
    label: Mapped[int] = mapped_column(nullable=True)
