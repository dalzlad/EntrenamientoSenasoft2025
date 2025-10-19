# Pydantic
from pydantic import BaseModel
# Python
from decimal import Decimal


class Model(BaseModel):
    codigo: int
    nombre: str
    precio: Decimal
    stock: int
    estado: bool

    class Config:
        from_attributes = True
        json_encoders = {
            Decimal: lambda v: format(v, "f")
        }
