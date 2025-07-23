from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from app.database import Base

class Corral(Base):
    __tablename__ = "corrales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    limite_animales = Column(Integer, nullable=False, default=10)
    subdivisiones = Column(JSON, default=list)
    
    animales = relationship("Animal", back_populates="corral")


