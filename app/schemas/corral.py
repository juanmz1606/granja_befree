from pydantic import BaseModel
from typing import List, Optional


class CorralBase(BaseModel):
    nombre: str
    limite_animales: int
    subdivisiones: List[str] = []


class CorralCreate(CorralBase):
    pass


class CorralUpdate(BaseModel):
    nombre: Optional[str] = None
    limite_animales: Optional[int] = None
    subdivisiones: Optional[List[str]] = None


class CorralOut(CorralBase):
    id: int

    class Config:
        from_attributes  = True
