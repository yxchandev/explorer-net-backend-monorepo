"""Menu ORM model."""

from decimal import Decimal

from sqlalchemy import Enum, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from packages.pylib.src.models.enums import Currency
from packages.pylib.src.orm.base import TimestampedBase
from packages.pylib.src.orm.outlet import Outlet


class Menu(TimestampedBase):
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    outlet_id: Mapped[int] = mapped_column(
        ForeignKey("outlets.id"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    currency: Mapped[Currency] = mapped_column(
        Enum(Currency, name="currency_enum", native_enum=False, length=3),
        nullable=False,
    )
    category: Mapped[str] = mapped_column(String(255), nullable=False)

    outlet: Mapped[Outlet] = relationship("Outlet")
