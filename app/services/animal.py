from sqlalchemy.orm import Session
from app import models, schemas
from app.services.movimiento import registrar_movimiento

def crear_animal(db: Session, data: schemas.AnimalCreate):
    nuevo = models.Animal(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    registrar_movimiento(
        db,
        tipo_operacion="crear",
        entidad="Animal",
        detalle=nuevo.__dict__
    )

    return nuevo

def listar_animales(db: Session):
    return db.query(models.Animal).all()

def actualizar_animal(db: Session, animal_id: int, data: schemas.AnimalUpdate):
    animal = db.query(models.Animal).get(animal_id)
    if not animal:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(animal, key, value)

    db.commit()
    db.refresh(animal)

    registrar_movimiento(
        db,
        tipo_operacion="editar",
        entidad="Animal",
        detalle=animal.__dict__
    )

    return animal

def eliminar_animal(db: Session, animal_id: int):
    animal = db.query(models.Animal).get(animal_id)
    if not animal:
        return None

    registrar_movimiento(
        db,
        tipo_operacion="eliminar",
        entidad="Animal",
        detalle=animal.__dict__
    )

    db.delete(animal)
    db.commit()
    return True
