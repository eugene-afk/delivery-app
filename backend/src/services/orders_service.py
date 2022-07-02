from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..tables.orders_table import Order, OrderProduct
from ..database import get_session
from ..schemas.orders_schema import CreateOrder
from ..logger import logger

class OrdersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_orders_by_email(self, search) -> List[Order]:
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        try:
            orders = (
                self.session
                .query(Order)
                .filter(Order.email == search)
                .all()
            )
            return orders
        except Exception as ex:
            logger.exception(ex)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    def create_order(self, data: CreateOrder) -> Order:
        try:
            order = Order(**data.dict(exclude={'order_products'}))
            self.session.add(order)
            self.session.commit()

            for i in data.order_products:
                order_product = OrderProduct(
                    order_id = int(order.id),
                    product_id = i.product_id,
                    qty = i.qty
                )
                self.session.add(order_product)
                self.session.commit()
        except Exception as ex:
            logger.exception(ex)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return order