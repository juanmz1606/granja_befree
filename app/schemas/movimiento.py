from pydantic import BaseModel
from datetime import datetime


class MovimientoOut(BaseModel):
    id: int
    fecha: datetime
    tipo_operacion: str
    entidad: str
    detalle_json: str

    class Config:
        from_attributes  = True
