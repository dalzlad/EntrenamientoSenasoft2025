# FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# Settings
from app.core.settings import settings
# Products
from app.features.productos.presentation import ProductsRouter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Products
app.include_router(ProductsRouter.router, prefix="/api/v1", tags=["Productos"])
