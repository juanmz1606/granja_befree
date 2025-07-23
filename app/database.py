from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Motor de conexión a la base de datos
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}  # necesario para SQLite
)

# Sesión local para cada request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()
