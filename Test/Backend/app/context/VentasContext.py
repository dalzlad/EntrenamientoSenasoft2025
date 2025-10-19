from typing import Optional
import decimal

from sqlalchemy import BigInteger, Boolean, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Core
from app.core.database import Base


class Clientes(Base):
    __tablename__ = 'clientes'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='clientes_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    apellido: Mapped[str] = mapped_column(String(250), nullable=False)
    correo: Mapped[str] = mapped_column(String(250), nullable=False)
    telefono: Mapped[str] = mapped_column(String(250), nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))

    pedidos: Mapped[list['Pedidos']] = relationship('Pedidos', back_populates='clientes')


class Productos(Base):
    __tablename__ = 'productos'
    __table_args__ = (
        PrimaryKeyConstraint('codigo', name='productos_pkey'),
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(250), nullable=False)
    precio: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 0), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))

    detalles_pedido: Mapped[list['DetallesPedido']] = relationship('DetallesPedido', back_populates='productos')


class Pedidos(Base):
    __tablename__ = 'pedidos'
    __table_args__ = (
        ForeignKeyConstraint(['id_cliente'], ['clientes.id'], name='pedidos_id_cliente_fkey'),
        PrimaryKeyConstraint('codigo', name='pedidos_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_cliente: Mapped[int] = mapped_column(BigInteger)
    total: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 0))
    estado: Mapped[bool] = mapped_column(Boolean, server_default=text('true'))

    clientes: Mapped['Clientes'] = relationship('Clientes', back_populates='pedidos')
    detalles_pedido: Mapped[list['DetallesPedido']] = relationship('DetallesPedido', back_populates='pedidos')


class DetallesPedido(Base):
    __tablename__ = 'detalles_pedido'
    __table_args__ = (
        ForeignKeyConstraint(['codigo_pedido'], ['pedidos.codigo'], name='detalles_pedido_codigo_pedido_fkey'),
        ForeignKeyConstraint(['codigo_producto'], ['productos.codigo'], name='detalles_pedido_codigo_producto_fkey'),
        PrimaryKeyConstraint('codigo', name='detalles_pedido_pkey')
    )

    codigo: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    codigo_pedido: Mapped[int] = mapped_column(BigInteger)
    codigo_producto: Mapped[int] = mapped_column(BigInteger)
    subtotal: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 0))

    pedidos: Mapped['Pedidos'] = relationship('Pedidos', back_populates='detalles_pedido')
    productos: Mapped['Productos'] = relationship('Productos', back_populates='detalles_pedido')
