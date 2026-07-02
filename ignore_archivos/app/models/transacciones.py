from pydantic import BaseModel
from typing import Optional

# Modelo base de transacciones
class TransaccionBase(BaseModel):
    cliente_id: int
    monto: float
    descripcion: Optional[str] = None

# Modelo para crear una transacción
class TransaccionCrear(TransaccionBase):
    pass

# Modelo final de transacción con ID
class Transaccion(TransaccionBase):
    id: Optional[int] = None