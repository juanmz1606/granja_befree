from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime, timezone
from app.database import Base

class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    tipo_operacion = Column(String, nullable=False)
    entidad = Column(String, nullable=False)
    detalle_json = Column(Text, nullable=False)
