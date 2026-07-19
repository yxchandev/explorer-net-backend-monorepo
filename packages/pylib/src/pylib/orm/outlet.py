"""Outlet ORM model."""

from decimal import Decimal

from sqlalchemy import Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pylib.models.enums import Country
from pylib.orm.base import TimestampedBase
from pylib.orm.client import Client


class Outlet(TimestampedBase):
    __tablename__ = "outlets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country: Mapped[Country] = mapped_column(
        Enum(Country, name="country_enum", native_enum=False, length=3),
        nullable=False,
    )
    unit: Mapped[str] = mapped_column(String(255), nullable=False)
    address1: Mapped[str] = mapped_column(String(255), nullable=False)
    address2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    postcode: Mapped[str] = mapped_column(String(32), nullable=False)
    latitude: Mapped[Decimal] = mapped_column(Numeric(10, 7), nullable=False)
    longitude: Mapped[Decimal] = mapped_column(Numeric(10, 7), nullable=False)
    phone_number: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    client_id: Mapped[int] = mapped_column(
        ForeignKey("clients.id"),
        nullable=False,
        index=True,
    )

    client: Mapped[Client] = relationship("Client")
