from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Movimiento
from app.database import SessionLocal
from app.schemas.movimiento import MovimientoOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[MovimientoOut])
def listar_movimientos(db: Session = Depends(get_db)):
    return db.query(Movimiento).order_by(Movimiento.fecha.desc()).all()
