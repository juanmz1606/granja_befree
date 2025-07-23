from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.animal import AnimalCreate, AnimalUpdate, AnimalOut
from app.services import animal
from app.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AnimalOut)
def crear_animal(data: AnimalCreate, db: Session = Depends(get_db)):
    return animal.crear_animal(db, data)

@router.get("/", response_model=list[AnimalOut])
def listar_animales(db: Session = Depends(get_db)):
    return animal.listar_animales(db)

@router.put("/{animal_id}", response_model=AnimalOut)
def actualizar_animal(animal_id: int, data: AnimalUpdate, db: Session = Depends(get_db)):
    result = animal.actualizar_animal(db, animal_id, data)
    if result is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return result

@router.delete("/{animal_id}")
def eliminar_animal(animal_id: int, db: Session = Depends(get_db)):
    result = animal.eliminar_animal(db, animal_id)
    if not result:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return {"mensaje": "Animal eliminado correctamente"}
