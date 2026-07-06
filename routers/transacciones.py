from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.modelos.Transacciones import Transaccion, TransaccionCrear, TransaccionRead, ListaTransacciones # <--- IMPORTANTE: Importa TransaccionRead y ListaTransacciones
from app.conexion_bd import get_session
from app.modelos.Facturas import Factura # Asegúrate de que esta ruta sea la correcta

router = APIRouter(
    prefix="/transacciones",
    tags=["transacciones"]
)

@router.get("/", response_model=ListaTransacciones)
def listar_transacciones(session: Session = Depends(get_session)):
    transacciones = session.exec(select(Transaccion)).all()

    resultado = []
    total_general = 0

    for t in transacciones:
        total = t.cantidad * t.valor_unitario
        total_general += total

        # Calcular subtotal de la factura (suma de todas las transacciones de esa factura)
        transacciones_factura = session.exec(
            select(Transaccion).where(Transaccion.factura_id == t.factura_id)
        ).all()
        subtotal = sum(tr.cantidad * tr.valor_unitario for tr in transacciones_factura)
        
        # Obtener el valor total (monto) de la factura
        factura = session.get(Factura, t.factura_id)
        valor_total = factura.monto if factura else 0

        resultado.append(
            TransaccionRead(
                id=t.id,
                factura_id=t.factura_id,
                cantidad=t.cantidad,
                valor_unitario=t.valor_unitario,
                descripcion=t.descripcion,
                total=total,
                subtotal=subtotal,
                valor_total=valor_total
            )
        )

    return ListaTransacciones(
        transacciones=resultado,
        total_general=total_general
    )

@router.post("/", response_model=TransaccionRead)
def crear_transaccion(datos_transaccion: TransaccionCrear, session: Session = Depends(get_session)):
    factura = session.get(Factura, datos_transaccion.factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="La factura no existe")

    transaccion = Transaccion.model_validate(datos_transaccion)
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    
    # Retornamos directamente el modelo de lectura con el cálculo
    total_calculado = transaccion.cantidad * transaccion.valor_unitario
    
    # Calcular subtotal de la factura
    transacciones_factura = session.exec(
        select(Transaccion).where(Transaccion.factura_id == transaccion.factura_id)
    ).all()
    subtotal = sum(tr.cantidad * tr.valor_unitario for tr in transacciones_factura)
    
    return TransaccionRead(
        id=transaccion.id,
        factura_id=transaccion.factura_id,
        cantidad=transaccion.cantidad,
        valor_unitario=transaccion.valor_unitario,
        descripcion=transaccion.descripcion,
        total=total_calculado,
        subtotal=subtotal,
        valor_total=factura.monto
    )

@router.get("/{id}", response_model=TransaccionRead)
def obtener_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    
    # Retornamos directamente el modelo de lectura
    total_calculado = transaccion.cantidad * transaccion.valor_unitario
    
    # Calcular subtotal de la factura
    transacciones_factura = session.exec(
        select(Transaccion).where(Transaccion.factura_id == transaccion.factura_id)
    ).all()
    subtotal = sum(tr.cantidad * tr.valor_unitario for tr in transacciones_factura)
    
    # Obtener el valor total (monto) de la factura
    factura = session.get(Factura, transaccion.factura_id)
    valor_total = factura.monto if factura else 0
    
    return TransaccionRead(
        id=transaccion.id,
        factura_id=transaccion.factura_id,
        cantidad=transaccion.cantidad,
        valor_unitario=transaccion.valor_unitario,
        descripcion=transaccion.descripcion,
        total=total_calculado,
        subtotal=subtotal,
        valor_total=valor_total
    )

@router.put("/{id}", response_model=TransaccionRead)
def actualizar_transaccion(id: int, datos_transaccion: TransaccionCrear, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    factura = session.get(Factura, datos_transaccion.factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="La factura no existe")

    transaccion.factura_id = datos_transaccion.factura_id
    transaccion.cantidad = datos_transaccion.cantidad
    transaccion.valor_unitario = datos_transaccion.valor_unitario
    transaccion.descripcion = datos_transaccion.descripcion

    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)
    
    # Retornamos el modelo de lectura actualizado
    total_calculado = transaccion.cantidad * transaccion.valor_unitario
    
    # Calcular subtotal de la factura
    transacciones_factura = session.exec(
        select(Transaccion).where(Transaccion.factura_id == transaccion.factura_id)
    ).all()
    subtotal = sum(tr.cantidad * tr.valor_unitario for tr in transacciones_factura)
    
    return TransaccionRead(
        id=transaccion.id,
        factura_id=transaccion.factura_id,
        cantidad=transaccion.cantidad,
        valor_unitario=transaccion.valor_unitario,
        descripcion=transaccion.descripcion,
        total=total_calculado,
        subtotal=subtotal,
        valor_total=factura.monto
    )

@router.delete("/{id}")
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    session.delete(transaccion)
    session.commit()
    return {"mensaje": "Transacción eliminada correctamente"}