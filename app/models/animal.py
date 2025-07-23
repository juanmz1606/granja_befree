from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Animal(Base):
    __tablename__ = "animales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    fecha_ingreso = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    corral_id = Column(Integer, ForeignKey("corrales.id"))
    corral = relationship("Corral", back_populates="animales")


