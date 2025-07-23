# Sistema de Gestión de Granja - FastAPI

Este es un proyecto de backend construido con **Python y FastAPI** que permite gestionar los corrales de una granja, los animales que habitan en ellos y un histórico de movimientos para auditar cada operación realizada.

---

## Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Pydantic 2](https://docs.pydantic.dev/)
- [pydantic-settings](https://docs.pydantic.dev/latest/integrations/settings/)
- Python 3.11+

---

Instalación y ejecución local

1.Clona el repositorio

git clone https://github.com/juanmz1606/granja_befree.git

cd granja_befree

2.Crea y activa el entorno virtual

python -m venv venv

# Windows Git Bash
source venv/Scripts/activate

# Linux / WSL / PowerShell
source venv/bin/activate

3.Instala las dependencias

pip install -r requirements.txt

4.Ejecuta el servidor

uvicorn app.main:app --reload
Abre el navegador y visita 👉 http://localhost:8000/docs


# Base de datos

Este sistema usa SQLite por defecto (app.db) y guarda toda la información localmente. Los datos persisten incluso si detienes la aplicación, siempre que no elimines el archivo .db.