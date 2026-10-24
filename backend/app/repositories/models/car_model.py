from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Car(Base):
    __tablename__ = 'car'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    car_brand: Mapped[str] = mapped_column(String(32), nullable=False)
    model: Mapped[str] = mapped_column(String(64), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(String(32), nullable=False)
    reg_number: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    mileage: Mapped[int] = mapped_column(nullable=False)
    last_service_date: Mapped[date] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self.id}, reg_number: {self.reg_number})"
