from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

from ..tables.orders_table import OrderStatusEnum
from ..schemas.shops_schema import ShopProduct

class OrderBase(BaseModel):
    email: str
    phone: str
    name: str
    desc: Optional[str]
    address: str
    shop_id: int
    amount: str

class OrderProductCart(BaseModel):
    product_id: int
    qty: int

class CreateOrder(OrderBase):
    order_products: List[OrderProductCart]

class OrderProduct(BaseModel):
    id: int
    product: ShopProduct
    qty: int
    class Config:
	    orm_mode=True

class Order(OrderBase):
    id: int
    date: datetime
    status: OrderStatusEnum
    amount: str
    products: List[OrderProduct] = []
    class Config:
	    orm_mode=True