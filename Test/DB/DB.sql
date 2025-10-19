CREATE TABLE clientes (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(250) NOT NULL,
    apellido VARCHAR(250) NOT NULL,
    correo VARCHAR(250) NOT NULL,
    telefono VARCHAR(250) NOT NULL,
    estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE productos (
    codigo BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(250) NOT NULL,
    precio NUMERIC(10, 0) NOT NULL,
    stock INTEGER NOT NULL,
    estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE pedidos (
    codigo BIGSERIAL PRIMARY KEY,
    id_cliente BIGINT NOT NULL,
    total NUMERIC(10, 0),
    estado BOOLEAN DEFAULT TRUE,
    CONSTRAINT pedidos_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES clientes (id)
);

CREATE TABLE detalles_pedido (
    codigo BIGSERIAL PRIMARY KEY,
    cantidad INTEGER NOT NULL,
    codigo_pedido BIGINT NOT NULL,
    codigo_producto BIGINT NOT NULL,
    subtotal NUMERIC(10, 0),
    CONSTRAINT detalles_pedido_codigo_pedido_fkey FOREIGN KEY (codigo_pedido) REFERENCES pedidos (codigo),
    CONSTRAINT detalles_pedido_codigo_producto_fkey FOREIGN KEY (codigo_producto) REFERENCES productos (codigo)
);
