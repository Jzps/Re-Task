from database.config import SessionLocal
from crud import auto_crud
from schemas.auto_schema import AutoCreate
from autos import AutoNuevo, AutoUsado, AutoElectrico

# ============================================
# CLASE CONCESIONARIO
# Encapsula la lógica de negocio del sistema.
# Se comunica con la BD a través de crud
# y crea objetos de autos según el tipo.
# ============================================

class Concesionario:
    def __init__(self):
        # Se crea una sesión de BD por instancia del concesionario
        self.db = SessionLocal()

    # --------------------------------------------
    # COMPRAR AUTO: registrar en la BD
    # --------------------------------------------
    def comprar_auto(self, auto):
        """
        Recibe un objeto de tipo Auto (Nuevo, Usado, Eléctrico),
        lo transforma en un esquema Pydantic (AutoCreate),
        y lo guarda en la BD usando crud.
        """
        auto_schema = AutoCreate(
            marca=auto.marca,
            modelo=auto.modelo,
            precio=auto.precio,
            tipo=auto.__class__.__name__,   # Guardamos el tipo de clase: AutoNuevo, AutoUsado, AutoElectrico
            extra=str(getattr(auto, "kilometraje", getattr(auto, "autonomia", None)))
        )
        auto_crud.crear_auto(self.db, auto_schema)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    # --------------------------------------------
    # MOSTRAR AUTOS: listar los registrados en la BD
    # --------------------------------------------
    def mostrar_autos(self):
        """
        Obtiene todos los autos de la BD y los muestra.
        """
        autos = auto_crud.obtener_autos(self.db)
        if not autos:
            print("No hay autos en el concesionario.")
        else:
            for i, auto in enumerate(autos, start=1):
                print(f"{i}. {auto.marca} {auto.modelo} ({auto.tipo}) - ${auto.precio}")

    # --------------------------------------------
    # VENDER AUTO: eliminarlo de la BD
    # --------------------------------------------
    def vender_auto(self, indice: int):
        """
        Vende (elimina) un auto según su índice en la lista.
        """
        autos = auto_crud.obtener_autos(self.db)
        if 0 <= indice - 1 < len(autos):
            auto = autos[indice - 1]
            eliminado = auto_crud.eliminar_auto(self.db, auto.id)
            print(f"Se ha vendido: {eliminado.marca} {eliminado.modelo}")
        else:
            print("Índice inválido, no se pudo vender el auto.")

    # --------------------------------------------
    # DAR MANTENIMIENTO: depende del tipo de auto
    # --------------------------------------------
    def dar_mantenimiento(self, indice: int):
        """
        Reconstruye el objeto Auto a partir de lo almacenado en la BD
        y ejecuta su método de mantenimiento.
        """
        autos = auto_crud.obtener_autos(self.db)
        if 0 <= indice - 1 < len(autos):
            auto_db = autos[indice - 1]

            # Reconstruimos el objeto dinámicamente según el tipo guardado
            if auto_db.tipo == "AutoNuevo":
                auto_obj = AutoNuevo(auto_db.marca, auto_db.modelo, auto_db.precio)
            elif auto_db.tipo == "AutoUsado":
                auto_obj = AutoUsado(auto_db.marca, auto_db.modelo, auto_db.precio, int(auto_db.extra))
            elif auto_db.tipo == "AutoElectrico":
                auto_obj = AutoElectrico(auto_db.marca, auto_db.modelo, auto_db.precio, int(auto_db.extra))
            else:
                print("Tipo de auto no reconocido.")
                return

            # Llamamos al mantenimiento específico
            resultado = auto_obj.dar_mantenimiento()
            print(resultado)
        else:
            print("Índice inválido, no se pudo dar mantenimiento.")
