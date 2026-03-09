import datetime
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.db.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now,
        nullable=False
    )