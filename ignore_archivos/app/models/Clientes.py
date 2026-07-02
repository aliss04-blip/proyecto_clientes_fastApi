from pydantic import BaseModel
from typing import Optional

# Modelo base con los datos principales del cliente
class ClienteBase(BaseModel):
    nombre: str
    edad: int
    descripcion: Optional[str] = None

# Modelo para crear un cliente
class ClienteCrear(ClienteBase):
    pass

# Modelo completo del cliente (incluye ID)
class Cliente(ClienteBase):
    id: Optional[int] = None