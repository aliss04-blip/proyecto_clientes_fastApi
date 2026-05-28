# PROYECTO FASTAPI CLIENTES

## Información del estudiante

* Nombre: Alison Valeria Garzón
* Número de ficha: 3407184

---

# Descripción del proyecto

Este proyecto fue desarrollado con FastAPI y permite realizar operaciones CRUD para:

* Clientes
* Facturas
* Transacciones

La aplicación permite:

* Crear registros
* Listar información
* Editar datos
* Eliminar registros

---

# Estructura de carpetas

```text
proyecto_clientes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   └── facturas.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── clientes.py
│
├── venv/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Historial de actividades realizadas

1. Creación de la carpeta principal del proyecto.
2. Creación y activación del entorno virtual.
3. Instalación de FastAPI y Uvicorn.
4. Organización de carpetas y archivos.
5. Creación de modelos con Pydantic.
6. Desarrollo de endpoints CRUD:
  * Clientes
  * Facturas
  * Transacciones
7. Pruebas de funcionamiento en Swagger.
8. Configuración de Git y GitHub.
9. Creación del archivo README.md.
10. Configuración del archivo .gitignore.

---

# Instalación del proyecto

## Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## Entrar a la carpeta

```bash
cd proyecto_clientes
```

---

# Crear entorno virtual

```bash
python -m venv venv
```

---

# Activar entorno virtual

## En Git Bash

```bash
source venv/Scripts/activate
```

## En PowerShell

```powershell
.\venv\Scripts\Activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

---

# Abrir en el navegador

## API

```text
http://127.0.0.1:8000
```

## Documentación Swagger

```text
http://127.0.0.1:8000/docs
```
