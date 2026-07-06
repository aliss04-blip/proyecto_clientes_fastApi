# Sistema de Gestión SENA - API Unificada 🚀

## Información del Aprendiz

- **Nombre:**Alison Valeria Garzon
- **Ficha:3407184
- **Instructor:** Jhony Guerrero

---

# 🛠️ Descripción del Proyecto

Este proyecto consiste en una **API REST** desarrollada con **FastAPI** y **SQLModel** para administrar **Clientes, Facturas y Transacciones**. La aplicación implementa una arquitectura modular, siguiendo buenas prácticas de programación, validación de datos y persistencia en una base de datos SQLite.

---

# 📐 Arquitectura y Buenas Prácticas Aplicadas

### ✅ Modularización con APIRouter
Los endpoints se encuentran organizados en módulos independientes dentro de la carpeta `routers`, manteniendo el archivo `main.py` limpio y fácil de mantener.

### ✅ Modelos con SQLModel
Se utilizan modelos de SQLModel para representar las tablas de la base de datos, combinando las ventajas de SQLAlchemy y Pydantic.

### ✅ Validación Automática
Los datos enviados por el cliente son validados automáticamente mediante Pydantic, garantizando la integridad de la información.

### ✅ Persistencia de Datos
La información se almacena en una base de datos SQLite utilizando sesiones (`Session`) y un motor (`Engine`) configurados en `conexion_bd.py`.

### ✅ Integridad Referencial
Las tablas Facturas y Transacciones incluyen llaves foráneas hacia la tabla Clientes para mantener relaciones consistentes.

---

# 📂 Estructura del Proyecto

```
PROYECTO_CLIENTES_FASTAPI/
│
├── .gitignore
├── requirements.txt
├── README.md
│
└── app/
    ├── __init__.py
    ├── main.py
    ├── conexion_bd.py
    ├── models/
    │   ├── clientes.py
    │   ├── facturas.py
    │   └── transacciones.py
    └── routers/
        ├── clientes.py
        ├── facturas.py
        └── transacciones.py
```

---

# 💾 Implementación de Persistencia con SQLModel

## Configuración de Base de Datos

- Implementación de `create_engine()`.
- Uso de `Session` para gestionar las operaciones sobre la base de datos.
- Base de datos SQLite.
- Configuración de `check_same_thread=False`.
- Creación automática de tablas mediante `crear_bd()`.

---

## Modelos

Se implementaron los modelos:

- Cliente
- Factura
- Transacción

Cada modelo utiliza:

- `SQLModel`
- `Field`
- Llaves primarias
- Llaves foráneas
- Relaciones entre tablas

---

## Routers

Cada módulo implementa un CRUD completo:

### Clientes

- Crear cliente
- Consultar clientes
- Consultar cliente por ID
- Actualizar cliente
- Eliminar cliente

### Facturas

- Crear factura
- Consultar facturas
- Consultar factura por ID
- Actualizar factura
- Eliminar factura

### Transacciones

- Crear transacción
- Consultar transacciones
- Consultar transacción por ID
- Actualizar transacción
- Eliminar transacción

---

# 🚀 Tecnologías Utilizadas

- Python 3
- FastAPI
- SQLModel
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

---

# ▶️ Ejecución del Proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
uvicorn app.main:app --reload
```

Abrir la documentación automática:

```
http://127.0.0.1:8000/docs
```

Documentación alternativa:

```
http://127.0.0.1:8000/redoc
```

---

# 📌 Estado del Proyecto

✅ Proyecto completamente funcional.

Incluye:

- API REST
- Persistencia en SQLite
- CRUD completo
- Validación de datos
- Arquitectura modular
- Integridad referencial entre tablas
- Documentación automática con Swagger
- CORS habilitado
- Búsqueda de clientes por nombre

---

# 👩‍💻 Desarrollado por

**Alison Valeria**

**SENA - Análisis y Desarrollo de Software**

**Instructor:** Jhony Guerrero

---

## ¡Gracias Instructor Jhony Guerrero!