from fastapi import APIRouter

from .root_router import root_router
from .car_router import car_router
from .consumables_router import consumables_router


routers = APIRouter()
routers.include_router(root_router)
routers.include_router(car_router)
routers.include_router(consumables_router)


__all__ = ['routers']
