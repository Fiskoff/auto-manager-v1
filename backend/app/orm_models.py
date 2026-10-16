import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = 'car'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    car_brand: Mapped[str] = mapped_column(String(32), nullable=False)
    model: Mapped[str] = mapped_column(String(64), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    colour: Mapped[str] = mapped_column(String(32), nullable=False)
    reg_number: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    mileage: Mapped[int] = mapped_column(nullable=False)
    data_last_maintenance_service:  Mapped[datetime.date] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self.id}, reg_number:{self.reg_number})"


class Consumables(Base):
    __tablename__ = 'consumables'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    start_mileage: Mapped[int] = mapped_column(nullable=False)
    end_mileage: Mapped[int] = mapped_column(nullable=True)
    start_date: Mapped[datetime.date] = mapped_column(nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(nullable=True)
    car_id: Mapped[int] = mapped_column(ForeignKey(Car.id), nullable=False)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self.id}, car_id:{self.car_id})"

