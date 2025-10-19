# FastAPI
from fastapi import APIRouter
# UOW
from app.core.unit_of_work import UnitOfWork
# Application
from app.features.productos.application.GetAll import GetAll
from app.features.productos.application.GetByCode import GetByCode
from app.features.productos.application.Add import Add
from app.features.productos.application.Modify import Modify
from app.features.productos.application.Delete import Delete
# DTOs
from app.features.productos.DTOs.SendDTO import SendDTO


router = APIRouter()


@router.get('/products')
async def get_all():
    async with UnitOfWork() as uow:
        use_case = GetAll(uow)
        return await use_case.execute_async()


@router.get('/products/{code}')
async def get_by_code(code: int):
    async with UnitOfWork() as uow:
        use_case = GetByCode(uow)
        return await use_case.execute_async(code)
    
    
@router.post('/products')
async def add(product: SendDTO):
    async with UnitOfWork() as uow:
        use_case = Add(uow)
        return await use_case.execute_async(product)
    

@router.put('/products/{code}')
async def modify(code: int, product: SendDTO):
    async with UnitOfWork() as uow:
        use_case = Modify(uow)
        return await use_case.execute_async(code, product)
    

@router.delete('/products/{code}')
async def delete(code: int):
    async with UnitOfWork() as uow:
        use_case = Delete(uow)
        return await use_case.execute_async(code)
