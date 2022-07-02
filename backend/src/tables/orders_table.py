from sqlalchemy import Column, String, Integer, Enum, DateTime 
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
import enum

from .base import Base

class OrderStatusEnum(enum.Enum):
    Pending = 1,
    Accepted = 2,
    Ended = 3,
    Canceled = 4

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    email = Column(String)
    phone = Column(String)
    name = Column(String)
    desc = Column(String, default="no desc.")
    address = Column(String)
    amount = Column(String, nullable=False)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.Pending)
    products = relationship("OrderProduct", backref="order")
    shop_id = Column(Integer, ForeignKey("shops.id"))
    product = relationship("Shop", backref=backref("order", uselist=False))

class OrderProduct(Base):
    __tablename__ = 'order_products'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    qty = Column(Integer, default=1)
    product_id = Column(Integer, ForeignKey("shop_products.id"))
    product = relationship("ShopProduct", backref=backref("orderproduct", uselist=False))