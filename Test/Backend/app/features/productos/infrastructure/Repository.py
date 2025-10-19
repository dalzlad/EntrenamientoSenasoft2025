# Python
from typing import List
# SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
# Context
from app.context.VentasContext import Productos
# DTOs
from app.features.productos.DTOs.GetDTO import GetDTO
from app.features.productos.DTOs.SendDTO import SendDTO
# Model
from app.features.productos.domain.Model import Model


class Repository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        products_list = await self.db.execute(select(Productos))
        products_list = products_list.scalars().all()

        return [GetDTO.model_validate(product) for product in products_list]
    
    async def get_by_code(self, code: int):
        product = await self.__get_by_code(code)

        if not product:
            raise

        return Model.model_validate(product)

    async def add(self, product: SendDTO):
        new_product = Productos(**product.dict())
        self.db.add(new_product)

        try:
            await self.db.flush()
            return Model.model_validate(new_product)
        except:
            raise

    async def modify(self, code: int, product: SendDTO):
        actual_product = await self.__get_by_code(code)

        if not actual_product:
            raise

        for key, value in product.dict().items():
            setattr(actual_product, key, value)
        
        try:
            await self.db.flush()
            return Model.model_validate(actual_product)
        except:
            raise

    async def remove(self, code: int):
        actual_product = await self.__get_by_code(code)

        try:
            await self.db.delete(actual_product)
            await self.db.flush()

            return Model.model_validate(actual_product)
        except:
            raise

    async def __get_by_code(self, code: int):
        product = await self.db.execute(select(Productos).where(Productos.codigo == code))
        product = product.scalars().first()

        if not product:
            raise

        return product