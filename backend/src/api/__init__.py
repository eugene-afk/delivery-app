from fastapi import APIRouter   

from .orders import router as orders_router
from .shops import router as shops_router

router = APIRouter()
router.include_router(orders_router)
router.include_router(shops_router)