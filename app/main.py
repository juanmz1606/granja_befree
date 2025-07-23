from fastapi import FastAPI
from app.routes import animal, corral, movimiento
from app.database import Base, engine

app = FastAPI()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(animal.router, prefix="/animales", tags=["Animales"])
app.include_router(corral.router, prefix="/corrales", tags=["Corrales"])
app.include_router(movimiento.router, prefix="/movimientos", tags=["Movimientos"])


@app.get("/")
def root():
    return {"mensaje": "¡La API de la granja está viva!"}
