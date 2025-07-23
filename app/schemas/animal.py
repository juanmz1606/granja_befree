from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AnimalBase(BaseModel):
    nombre: str
    tipo: str
    corral_id: int


class AnimalCreate(AnimalBase):
    pass


class AnimalUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    corral_id: Optional[int] = None


class AnimalOut(AnimalBase):
    id: int
    fecha_ingreso: datetime

    class Config:
        from_attributes  = True
