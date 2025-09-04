from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate

# ============================================
# Funciones CRUD (Create, Read, Delete) para
# manejar la tabla "Auto" en la base de datos
# ============================================

def crear_auto(db: Session, auto: AutoCreate):
    """
    Inserta un nuevo auto en la base de datos.
    :param db: sesión de la base de datos
    :param auto: objeto validado con Pydantic (AutoCreate)
    :return: el objeto Auto creado en la BD
    """
    db_auto = Auto(
        marca=auto.marca,
        modelo=auto.modelo,
        precio=auto.precio,
        tipo=auto.tipo,   # Tipo de auto: Nuevo, Usado o Eléctrico
        extra=auto.extra  # Información adicional (kilometraje, autonomía, etc.)
    )
    db.add(db_auto)      # Añade el objeto a la sesión
    db.commit()          # Confirma los cambios en la base de datos
    db.refresh(db_auto)  # Refresca el objeto con los datos definitivos (incluye el id autogenerado)
    return db_auto


def obtener_autos(db: Session):
    """
    Recupera todos los autos registrados en la base de datos.
    :param db: sesión de la base de datos
    :return: lista de autos (query result)
    """
    return db.query(Auto).all()


def eliminar_auto(db: Session, auto_id: int):
    """
    Elimina un auto de la base de datos según su id.
    :param db: sesión de la base de datos
    :param auto_id: identificador único del auto
    :return: el auto eliminado o None si no existe
    """
    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)   # Marca el auto para borrado
        db.commit()       # Aplica los cambios
    return auto
