from autos.base import Auto

# ============================================
# Clase para autos nuevos
# Hereda de Auto y agrega un método de mantenimiento
# ============================================
class AutoNuevo(Auto):
    def dar_mantenimiento(self):
        """
        Permite realizar opciones de mantenimiento
        específicas para autos nuevos.
        """
        print(f"\n--- Mantenimiento para Auto Nuevo {self.marca} {self.modelo} ---")
        print("1. Revisión básica")
        print("2. Lavado")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return f"El auto nuevo {self.marca} {self.modelo} recibió revisión básica."
        elif opcion == "2":
            return f"El auto nuevo {self.marca} {self.modelo} fue lavado."
        else:
            return "Opción inválida."


# ============================================
# Clase para autos usados
# Incluye el atributo "kilometraje" adicional
# ============================================
class AutoUsado(Auto):
    def __init__(self, marca, modelo, precio, kilometraje):
        """
        Constructor para autos usados.
        :param kilometraje: cantidad de kilómetros recorridos
        """
        super().__init__(marca, modelo, precio)
        self.kilometraje = kilometraje

    def mostrar_info(self):
        """
        Sobrescribe el método mostrar_info para
        agregar el kilometraje.
        """
        return super().mostrar_info() + f", Kilometraje: {self.kilometraje} km"

    def dar_mantenimiento(self):
        """
        Permite realizar mantenimiento específico
        para autos usados.
        """
        print(f"\n--- Mantenimiento para Auto Usado {self.marca} {self.modelo} ---")
        print("1. Cambio de aceite")
        print("2. Revisión general")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return f"El auto usado {self.marca} {self.modelo} recibió cambio de aceite."
        elif opcion == "2":
            return f"El auto usado {self.marca} {self.modelo} recibió revisión general."
        else:
            return "Opción inválida."


# ============================================
# Clase para autos eléctricos
# Incluye el atributo "autonomía" adicional
# ============================================
class AutoElectrico(Auto):
    def __init__(self, marca, modelo, precio, autonomia):
        """
        Constructor para autos eléctricos.
        :param autonomia: cantidad de km que puede recorrer con una carga
        """
        super().__init__(marca, modelo, precio)
        self.autonomia = autonomia

    def mostrar_info(self):
        """
        Sobrescribe el método mostrar_info para
        agregar la autonomía.
        """
        return super().mostrar_info() + f", Autonomía: {self.autonomia} km"

    def dar_mantenimiento(self):
        """
        Permite realizar mantenimiento específico
        para autos eléctricos.
        """
        print(f"\n--- Mantenimiento para Auto Eléctrico {self.marca} {self.modelo} ---")
        print("1. Revisión de batería")
        print("2. Actualización de software")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió revisión de batería."
        elif opcion == "2":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió actualización de software."
        else:
            return "Opción inválida."
