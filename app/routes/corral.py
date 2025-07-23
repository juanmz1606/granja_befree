from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.corral import CorralCreate, CorralUpdate, CorralOut
from app.services import corral
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CorralOut)
def crear_corral(data: CorralCreate, db: Session = Depends(get_db)):
    return corral.crear_corral(db, data)

@router.get("/", response_model=list[CorralOut])
def listar_corrales(db: Session = Depends(get_db)):
    return corral.listar_corrales(db)

@router.put("/{corral_id}", response_model=CorralOut)
def actualizar_corral(corral_id: int, data: CorralUpdate, db: Session = Depends(get_db)):
    result = corral.actualizar_corral(db, corral_id, data)
    if result is None:
        raise HTTPException(status_code=404, detail="Corral no encontrado")
    return result
