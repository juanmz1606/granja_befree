from sqlalchemy.orm import Session
from app.models import Movimiento
import json
from datetime import datetime, timezone

def registrar_movimiento(db: Session, tipo_operacion: str, entidad: str, detalle: dict):
    movimiento = Movimiento(
        tipo_operacion=tipo_operacion,
        entidad=entidad,
        detalle_json=json.dumps(detalle, default=str),
        fecha=datetime.now(timezone.utc)
    )
    db.add(movimiento)
    db.commit()
