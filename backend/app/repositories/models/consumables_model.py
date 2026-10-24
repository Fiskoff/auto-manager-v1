from datetime import date

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Consumables(Base):
    __tablename__ = 'consumables'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    start_mileage: Mapped[int] = mapped_column(nullable=False)
    end_mileage: Mapped[int] = mapped_column(nullable=True)
    start_date: Mapped[date] = mapped_column(nullable=False)
    end_date: Mapped[date] = mapped_column(nullable=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"), nullable=False)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self.id}, car_id: {self.car_id})"