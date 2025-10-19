# UOW
from app.core.unit_of_work import UnitOfWork
# Repository
from app.features.productos.infrastructure.Repository import Repository


class GetByCode:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.repository = Repository(self.uow.session)

    async def execute_async(self, code: int):
        return await self.repository.get_by_code(code)
        