from fastapi import FastAPI, HTTPException
from typing import List
# Importaciones exactas respetando mayúsculas y nombres de archivos
from app.models.Clientes import Cliente, ClienteCrear
from app.models.factura import Factura, FacturaCrear
from app.models.transacciones import Transaccion, TransaccionCrear

app = FastAPI(
    title="Sistema de Gestión SENA - JHONY",
    description="API unificada para la gestión de Clientes, Facturas y Transacciones",
    version="1.0.0"
)


# Listas globales en memoria con tipado correcto
lista_clientes: List[Cliente] = []
lista_facturas: List[Factura] = []
lista_transacciones: List[Transaccion] = []

@app.get("/")
def root():
    return {"mensaje": "¡API activa y funcionando correctamente!"}


# ==============================================================================
# ENDPOINTS DE CLIENTES
# ==============================================================================

@app.get("/clientes", tags=["Clientes"])
async def listar_clientes():
    return {"clientes": lista_clientes}


@app.post("/clientes", response_model=Cliente, tags=["Clientes"])
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes) + 1
    lista_clientes.append(cliente_val)
    return cliente_val


@app.get("/clientes/{id}", response_model=Cliente, tags=["Clientes"])
async def obtener_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.delete("/clientes/{id}", response_model=Cliente, tags=["Clientes"])
async def eliminar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            cliente_eliminado = Cliente.model_validate(cliente.model_dump())
            lista_clientes.remove(cliente)
            return cliente_eliminado
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.put("/clientes/{id}", response_model=Cliente, tags=["Clientes"])
async def actualizar_cliente(id: int, datos_cliente: ClienteCrear):
    for cliente in lista_clientes:
        if cliente.id == id:
            cliente_actualizado = Cliente(
                id=cliente.id,
                nombre=datos_cliente.nombre,
                edad=datos_cliente.edad,
                descripcion=datos_cliente.descripcion
            )
            index = lista_clientes.index(cliente)
            lista_clientes[index] = cliente_actualizado
            return cliente_actualizado
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ==============================================================================
# ENDPOINTS DE FACTURAS
# ==============================================================================

@app.get("/facturas", tags=["Facturas"])
async def listar_facturas():
    return {"facturas": lista_facturas}


@app.post("/facturas", response_model=Factura, tags=["Facturas"])
async def crear_factura(datos_factura: FacturaCrear):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.id = len(lista_facturas) + 1
    lista_facturas.append(factura_val)
    return factura_val


@app.get("/facturas/{id}", response_model=Factura, tags=["Facturas"])
async def obtener_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@app.delete("/facturas/{id}", response_model=Factura, tags=["Facturas"])
async def eliminar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            factura_eliminada = Factura.model_validate(factura.model_dump())
            lista_facturas.remove(factura)
            return factura_eliminada
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@app.put("/facturas/{id}", response_model=Factura, tags=["Facturas"])
async def actualizar_factura(id: int, datos_factura: FacturaCrear):
    for factura in lista_facturas:
        if factura.id == id:
            factura_actualizada = Factura(
                id=factura.id,
                cliente_id=datos_factura.cliente_id,
                monto=datos_factura.monto,
                descripcion=datos_factura.descripcion
            )
            index = lista_facturas.index(factura)
            lista_facturas[index] = factura_actualizada
            return factura_actualizada
    raise HTTPException(status_code=404, detail="Factura no encontrada")


# ==============================================================================
# ENDPOINTS DE TRANSACCIONES
# ==============================================================================

@app.get("/transacciones", tags=["Transacciones"])
async def listar_transacciones():
    return {"transacciones": lista_transacciones}


@app.post("/transacciones", response_model=Transaccion, tags=["Transacciones"])
async def crear_transaccion(datos_transaccion: TransaccionCrear):
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.id = len(lista_transacciones) + 1
    lista_transacciones.append(transaccion_val)
    return transaccion_val


@app.get("/transacciones/{id}", response_model=Transaccion, tags=["Transacciones"])
async def obtener_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            return transaccion
    raise HTTPException(status_code=404, detail="Transación no encontrada")


@app.delete("/transacciones/{id}", response_model=Transaccion, tags=["Transacciones"])
async def eliminar_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            transaccion_eliminada = Transaccion.model_validate(transaccion.model_dump())
            lista_transacciones.remove(transaccion)
            return transaccion_eliminada
    raise HTTPException(status_code=404, detail="Transación no encontrada")


@app.put("/transacciones/{id}", response_model=Transaccion, tags=["Transacciones"])
async def actualizar_transaccion(id: int, datos_transaccion: TransaccionCrear):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            transaccion_actualizada = Transaccion(
                id=transaccion.id,
                cliente_id=datos_transaccion.cliente_id,
                monto=datos_transaccion.monto,
                descripcion=datos_transaccion.descripcion
            )
            index = lista_transacciones.index(transaccion)
            lista_transacciones[index] = transaccion_actualizada
            return transaccion_actualizada
    raise HTTPException(status_code=404, detail="Transación no encontrada")