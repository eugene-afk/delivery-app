from typing import List
from fastapi import APIRouter, Depends 

from ..services.orders_service import OrdersService
from ..schemas.orders_schema import Order as OrderSchema, CreateOrder

router = APIRouter(
    prefix='/orders',
    tags=['Orders'],
)

@router.get('/', response_model=List[OrderSchema])
async def get_orders(search: str = "", service: OrdersService = Depends()):
    return service.get_orders_by_email(search)

@router.post('/', response_model=OrderSchema)
async def add_order(data: CreateOrder, service: OrdersService = Depends()):
    return service.create_order(data)