from typing import List
from fastapi import APIRouter, Depends

from ..services.shop_service import ShopsService
from ..schemas.shops_schema import Shop

router = APIRouter(
    prefix='/shops',
    tags=['Orders'],
)

@router.get('/', response_model=List[Shop])
async def get_shops(service: ShopsService = Depends()):
    return service.get_list()

@router.get('/makeshops', status_code=201)
async def make_shops(service: ShopsService = Depends()):
    return service.add_shops()
