# ============================================
# Clase base "Auto"
# Es la clase genérica de la cual heredan todos
# los tipos de autos (Nuevo, Usado, Eléctrico).
# ============================================

class Auto:
    def __init__(self, marca, modelo, precio):
        """
        Constructor de la clase Auto.
        :param marca: Marca del auto (ej: Toyota)
        :param modelo: Modelo del auto (ej: Corolla)
        :param precio: Precio del auto (ej: 15000.0)
        """
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        """
        Retorna un string con la información básica del auto.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"
