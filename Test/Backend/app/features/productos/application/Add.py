# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.productos.infrastructure.Repository import Repository
# DTOs
from app.features.productos.DTOs.SendDTO import SendDTO


class Add:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, product: SendDTO):
        return await self.repository.add(product)
        