from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from .car_model import Car
from .consumables_model import Consumables

__all__ = ['Base', 'Car', 'Consumables']