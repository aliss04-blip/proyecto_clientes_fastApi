from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import clientes, facturas, transacciones
from app.conexion_bd import crear_bd

app = FastAPI(title="API Alisson")

# Configuracion de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    crear_bd()

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)

@app.get("/")
def root():
    return {"mensaje": "Alisonn API - Hola mundo"}
