"""Page ORM model."""

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from packages.pylib.src.orm.base import TimestampedBase
from packages.pylib.src.orm.outlet import Outlet


class Page(TimestampedBase):
    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    outlet_id: Mapped[int] = mapped_column(
        ForeignKey("outlets.id"),
        nullable=False,
        index=True,
    )
    html: Mapped[str] = mapped_column(Text, nullable=False)

    outlet: Mapped[Outlet] = relationship("Outlet")
