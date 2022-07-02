from typing import List
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import random

from ..tables.shops_table import Shop, ShopProduct
from ..database import get_session
from ..logger import logger

class ShopsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[Shop]:
        try:
            shops = (
                self.session
                .query(Shop)
                .all()
            )
        except Exception as ex:
            logger.exception(ex)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return shops

    def add_shops(self) -> Shop:
        try:
            shop = (
                self.session
                .query(Shop)
                .first()
            )
            if shop:
                return Response(status_code=201)

            shops = []

            shop = Shop(
                address = "Khreshchatyk Street, 19-a, Kyiv",
                logo = "mc.png",
                name = "McDonalds",
                is_closed = False,
                lat = 50.44789327835881,
                lng = 30.522786207463845 
            )
            self.session.add(shop)
            self.session.commit()
            shops.append(shop)

            shop = Shop(
                address = "Mykola Bazhana Avenue, 1e, Kyiv",
                logo = "kfc.png",
                name = "KFC",
                is_closed = False,
                lat = 50.39586464621994,
                lng = 30.615584271164263
            )
            self.session.add(shop)
            self.session.commit()
            shops.append(shop)

            shop = Shop(
                address = "Velyka Vasylkivska Street, 72, Kyiv",
                logo = "salateira.jpg",
                name = "Salateira",
                is_closed = False,
                lat = 50.43234674901348,
                lng = 30.51510095767146 
            )
            self.session.add(shop)
            self.session.commit()
            shops.append(shop)

            shop = Shop(
                address = "Budivelnykiv Street, 40, Kyiv",
                logo = "puzata-hata.png",
                name = "Puzata Hata",
                is_closed = False,
                lat = 50.45490819439808,
                lng = 30.611183386507204 
            )
            self.session.add(shop)
            self.session.commit()
            shops.append(shop)

            shop = Shop(
                address = "Darnytsky Boulevard, 8A, Kyiv",
                logo = "silpo.png",
                name = "Silpo",
                is_closed = True,
                lat = 50.46464505275857,
                lng = 30.61025861534294 
            )
            self.session.add(shop)
            self.session.commit()
            shops.append(shop)

            for i in shops:
                cnt = 5
                for x in range(cnt):
                    product = ShopProduct(
                        name = f"{i.name } product #{x}",
                        price = str(random.randint(10, 500)),
                        photo = "food.jpg",
                        in_stock = False if x == 3 else True,
                        shop_parent_id = i.id
                    )
                    self.session.add(product)
                    self.session.commit()

            return Response(status_code=201)
        except Exception as ex:
            logger.exception(ex)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)