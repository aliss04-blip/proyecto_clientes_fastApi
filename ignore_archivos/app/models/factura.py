from pydantic import BaseModel
from typing import Optional

# Modelo base de factura
class FacturaBase(BaseModel):
    cliente_id: int
    monto: float
    descripcion: Optional[str] = None

# Modelo para crear una factura
class FacturaCrear(FacturaBase):
    pass

# Modelo final de factura con ID
class Factura(FacturaBase):
    id: Optional[int] = None