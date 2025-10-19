# Pydantic
from pydantic import BaseModel
# Python
from decimal import Decimal


class SendDTO(BaseModel):
    nombre: str
    precio: Decimal
    stock: int
    estado: bool
