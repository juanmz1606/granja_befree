from sqlalchemy.orm import Session
from app import models, schemas
from app.services.movimiento import registrar_movimiento

def crear_corral(db: Session, data: schemas.CorralCreate):
    nuevo = models.Corral(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    registrar_movimiento(
        db,
        tipo_operacion="crear",
        entidad="Corral",
        detalle=nuevo.__dict__
    )

    return nuevo

def listar_corrales(db: Session):
    return db.query(models.Corral).all()

def actualizar_corral(db: Session, corral_id: int, data: schemas.CorralUpdate):
    corral = db.query(models.Corral).get(corral_id)
    if not corral:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(corral, key, value)

    db.commit()
    db.refresh(corral)

    registrar_movimiento(
        db,
        tipo_operacion="editar",
        entidad="Corral",
        detalle=corral.__dict__
    )

    return corral
