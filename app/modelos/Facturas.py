from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from datetime import datetime

class Factura(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: date = Field(default_factory=lambda: datetime.now().date())
    cliente_id: int = Field(foreign_key="cliente.id") 
    monto: float = Field(gt=0)
    descripcion: Optional[str] = None

    # Relaciones: Una factura pertenece a un cliente y tiene muchas transacciones
    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: List["Transaccion"] = Relationship(back_populates="factura")

class FacturaCrear(SQLModel):
    fecha: Optional[date] = None
    cliente_id: int
    monto: float = Field(gt=0, description="El monto debe ser mayor a 0")
    descripcion: Optional[str] = None
