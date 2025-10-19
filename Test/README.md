# Sistema de Restaurante – Arquitectura Docker (React + FastAPI + PostgreSQL)

Este proyecto implementa un sistema base para la gestión de un restaurante, utilizando **React** para el frontend, **FastAPI** con **Clean Architecture** en el backend y **PostgreSQL** como base de datos.  
Todo está orquestado mediante **Docker Compose**, lo que permite levantar el entorno completo con un solo comando.

---

## Estructura del Proyecto

restaurant_fastapi/
│
├── frontend/ # Aplicación web en React
│ ├── src/
│ ├── package.json
│ └── Dockerfile
│
├── backend/ # API en FastAPI (Clean Architecture)
│ ├── app/
│ │ ├── core/ # Configuración principal
│ │ ├── domain/ # Entidades y modelos de negocio
│ │ ├── application/ # Casos de uso
│ │ ├── infrastructure/ # Adaptadores (DB, repositorios)
│ │ └── presentation/ # Rutas y controladores FastAPI
│ ├── create_tables.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── docs/ # Documentación técnica y funcional
│ ├── README.md
│ ├── arquitectura.png
│ ├── modelo_relacional.png
│ └── pruebas_funcionales.pdf
│
├── docker-compose.yml
├── .env
└── README.md


## Arquitectura General

La aplicación se compone de **tres servicios principales** (más uno de documentación), comunicados a través de la red interna de Docker.

                     ┌────────────────────────┐
                     │        FRONTEND        │
                     │    React (Node.js)     │
                     │------------------------│
                     │ Puerto: 3030           │
                     │ Carpeta: ./frontend    │
                     │ Reinicio: always       │
                     │                        │
                     │ Acceso desde navegador │
                     └───────────▲────────────┘
                        │
                        │ HTTP (fetch, axios)
                    ▼
┌────────────────────────┐ ┌────────────────────────┐
│ BACKEND                │ │ DB                     │
│ FastAPI (Python)       │ │ PostgreSQL 15          │
│------------------------│ │------------------------│
│ Puerto interno: 8000   │ │ Puerto interno: 5432   │
│ Expuesto: 8080         │ │ Expuesto: 5444         │
│ Env vars desde .env    │ │ Variables .env         │
│ ORM: SQLAlchemy        │ │ Volumen persistente    │
│ Reinicio: always       │ │ Reinicio: always       │
└───────────▲────────────┘ └──────────▲─────────────┘
           
                      ┌────────────────────┐
                      │     DOCUMENTACIÓN  │
                      │ Carpeta: ./docs/   │
                      │ Contiene:          │
                      │  - README.md       │
                      │  - Diagrama.png    │
                      │   │
                      │   │
                      └────────────────────┘


##  Configuración de Variables de Entorno (.env)

```env
# PostgreSQL
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=restaurant_db
DB_HOST=db
DB_PORT=5432

# Backend
BACKEND_PORT=8000

# Frontend
FRONTEND_PORT=3030
Despliegue con Docker Compose
1. Construir los contenedores

docker-compose build

2. Levantar los servicios

docker-compose up
3. Detener los servicios

docker-compose down
El backend se conectará automáticamente a la base de datos PostgreSQL y ejecutará los scripts iniciales definidos en create_tables.py.

Clean Architecture (Backend)
El backend está basado en los principios de Clean Architecture.
Esto garantiza un código desacoplado, fácil de mantener y escalar.

Capas principales:

Capa	                        Descripción
Domain	                        Entidades de negocio puras. Sin dependencias externas.
Application	                    Casos de uso (lógica de negocio).
Infrastructure	                Acceso a base de datos, frameworks y servicios externos.
Presentation	                Controladores, rutas y serialización de respuestas.

Tecnologías Principales
Componente	    Tecnología
Frontend	    React + Vite + Axios
Backend	        FastAPI + Python 3.11
Base de datos	PostgreSQL 15
Contenedores	Docker & Docker Compose
ORM	SQLAlchemy
Documentación	Markdown + PDF

Documentación
Toda la documentación técnica y de usuario se encuentra dentro del directorio docs/.
Ahí podrás ver el diagrama de arquitectura, manual técnico y manual de usuario.

Autores
Proyecto desarrollado como parte de SENASOFT 2025 – Categoría Desarrollo Libre.
Integrantes del equipo:

Johan – Arquitectura Backend (FastAPI, Docker)

Miguel  – Integración Frontend / Documentación

Ejemplo rápido de acceso
Frontend: http://localhost:3003

Backend API: http://localhost:8080/docs

Base de datos: localhost:5440