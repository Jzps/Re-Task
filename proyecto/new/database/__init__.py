# ============================================
# Este archivo inicializa el módulo "database"
# Reexporta las configuraciones principales y
# la función init_db para inicializar la BD.
#
# Permite hacer:
#   from database import SessionLocal, init_db
# ============================================

from .config import Base, SessionLocal, engine
from .database import init_db

__all__ = ["Base", "SessionLocal", "engine", "init_db"]
