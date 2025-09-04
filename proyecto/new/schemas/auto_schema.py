from pydantic import BaseModel

# ============================================
# SCHEMAS CON PYDANTIC
# Se usan para validar y estructurar la entrada
# y salida de datos (autos) antes de guardarlos
# o devolverlos desde la BD.
# ============================================

class AutoBase(BaseModel):
    """
    Esquema base para un Auto.
    Contiene los atributos comunes que deben existir
    al registrar o consultar un auto.
    """
    marca: str          # Marca del auto (ej: Toyota)
    modelo: str         # Modelo del auto (ej: Corolla)
    precio: float       # Precio del auto
    tipo: str           # Tipo de auto: Nuevo, Usado, Eléctrico
    extra: str | None = None  # Información extra (kilometraje/autonomía)

class AutoCreate(AutoBase):
    """
    Esquema para creación de autos.
    Hereda de AutoBase porque no necesita nada extra.
    """
    pass

class AutoOut(AutoBase):
    """
    Esquema para salida de datos.
    Incluye el ID del auto, que genera la BD.
    """
    id: int

    class Config:
        orm_mode = True  # Permite convertir objetos de SQLAlchemy a este esquema
