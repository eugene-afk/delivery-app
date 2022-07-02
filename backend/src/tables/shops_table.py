from sqlalchemy import Column, Float, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    address = Column(String, unique=True)
    logo = Column(String)
    is_closed = Column(Boolean, default=False) 
    lat = Column("lat", Float)
    lng = Column("lng", Float)
    products = relationship("ShopProduct", back_populates="owner")

class ShopProduct(Base):
    __tablename__ = 'shop_products'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(String, nullable=False)
    in_stock = Column(Boolean, default=True) 
    photo = Column(String)
    shop_parent_id = Column(Integer, ForeignKey("shops.id"))
    owner = relationship("Shop", back_populates="products")