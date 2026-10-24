from fastapi import APIRouter

from root_router import root_router
from car_router import car_router
from consumables_router import consumables_router


router = APIRouter()
router.include_router(root_router)
router.include_router(car_router)
router.include_router(consumables_router)


__all__ = ['router']
