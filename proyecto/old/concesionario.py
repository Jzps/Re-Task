# concesionario.py
class Concesionario:
    def __init__(self):
        # Lista que contiene los objetos Auto (o subclases)
        self.autos = []

    def comprar_auto(self, auto):
        # Añade el objeto auto a la lista y confirma la compra
        self.autos.append(auto)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    def vender_auto(self, indice):
        # Verifica que el índice esté dentro del rango válido
        if 0 <= indice < len(self.autos):
            auto_vendido = self.autos.pop(indice)  # Quita y devuelve el auto
            print(f"Se ha vendido: {auto_vendido.mostrar_info()}")
        else:
            print("Índice inválido, no se pudo vender el auto.")

    def mostrar_autos(self):
        # Muestra los autos. Si no hay ninguno, lo informa.
        if not self.autos:
            print("No hay autos en el concesionario.")
        else:
            # enumerate con start=1 para mostrar la lista al usuario comenzando en 1
            for i, auto in enumerate(self.autos, start = 1):
                print(f"{i}. {auto.mostrar_info()}")

    def dar_mantenimiento(self, indice):
        # Valida índice y llama al método dar_mantenimiento() del auto específico
        if 0 <= indice < len(self.autos):
            auto = self.autos[indice]
            # El método dar_mantenimiento() del auto pedirá la sub-opción y devolverá un string
            print(auto.dar_mantenimiento())
        else:
            print("Índice inválido, no se pudo dar mantenimiento.")
