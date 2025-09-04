from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ============================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ============================================

# Dirección de la base de datos (en este caso SQLite en un archivo local)
# Si quisieras usar Postgres sería algo como:
# postgresql://usuario:password@localhost:5432/mi_basedatos
DATABASE_URL = "sqlite:///./autos.db"

# Crea el motor de conexión a la base de datos
# echo=True permite ver en consola las consultas SQL ejecutadas
engine = create_engine(DATABASE_URL, echo=True)

# Crea una fábrica de sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base: clase base de la que heredan todos los modelos
Base = declarative_base()
