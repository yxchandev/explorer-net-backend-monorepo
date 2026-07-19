"""Client ORM model."""

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from pylib.orm.base import TimestampedBase


class Client(TimestampedBase):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    business_name: Mapped[str] = mapped_column(String(255), nullable=False)
    country_code: Mapped[int] = mapped_column(Integer, nullable=False)
    telephone: Mapped[int] = mapped_column(Integer, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    remark: Mapped[str | None] = mapped_column(Text, nullable=True)
    verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    reset_password: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
