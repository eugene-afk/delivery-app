from pydantic import BaseModel
from typing import List

class ShopBase(BaseModel):
    name: str
    address: str
    logo: str
    lat: float
    lng: float
    is_closed: bool

class ShopProductBase(BaseModel):
    name: str
    price: str


class ShopProduct(ShopProductBase):
    id: int    
    photo: str
    in_stock: bool
    class Config:
	    orm_mode=True

class Shop(ShopBase):
    id: int
    products: List[ShopProduct] = []
    class Config:
        orm_mode = True
