from database.config import Base, engine
from database.entities import auto  # Importa los modelos (asegura que se registren en Base)

# ============================================
# FUNCIÓN PARA INICIALIZAR LA BASE DE DATOS
# ============================================

def init_db():
    """
    Crea todas las tablas en la base de datos
    definidas en los modelos (entities).
    Si ya existen, no las recrea.
    """
    Base.metadata.create_all(bind=engine)
