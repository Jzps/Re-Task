# main.py
from tipos_autos import AutoNuevo, AutoUsado, AutoElectrico   # Importa las clases de autos específicas
from concesionario import Concesionario                      # Importa la clase Concesionario

def menu():
    concesionario = Concesionario()  # Crea una instancia del concesionario (lista de autos)

    while True:  # Bucle principal del programa - se repite hasta que el usuario elija salir
        print("\n--- MENÚ CONCESIONARIO ---")
        print("1. Comprar Auto")
        print("2. Vender Auto")
        print("3. Mostrar Autos")
        print("4. Dar Mantenimiento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")  # Lee la opción del usuario (string)

        if opcion == "1":  # COMPRAR AUTO
            print("\nTipos de Auto:")
            print("1. Nuevo")
            print("2. Usado")
            print("3. Eléctrico")

            tipo = input("Seleccione el tipo de auto: ")        # Tipo elegido por el usuario
            marca = input("Ingrese la marca: ")                  # Marca del auto
            modelo = input("Ingrese el modelo: ")                # Modelo del auto
            precio = float(input("Ingrese el precio: "))         # Precio (se convierte a float)

            if tipo == "1":  # Si es nuevo, se crea AutoNuevo con marca, modelo y precio
                auto = AutoNuevo(marca, modelo, precio)
            elif tipo == "2":  # Si es usado, pide kilometraje adicional y crea AutoUsado
                kilometraje = int(input("Ingrese el kilometraje: "))
                auto = AutoUsado(marca, modelo, precio, kilometraje)
            elif tipo == "3":  # Si es eléctrico, pide autonomía y crea AutoElectrico
                autonomia = int(input("Ingrese la autonomía de la batería (km): "))
                auto = AutoElectrico(marca, modelo, precio, autonomia)
            else:
                print("Tipo inválido.")  # Opción de tipo inválida
                continue  # Vuelve al inicio del bucle sin llamar a comprar_auto

            concesionario.comprar_auto(auto)  # Agrega el auto al concesionario

        elif opcion == "2":  # VENDER AUTO
            concesionario.mostrar_autos()  # Muestra la lista de autos (numerada desde 1)
            if concesionario.autos:  # Si hay autos disponibles
                indice = int(input("Ingrese el índice del auto a vender: "))- 1  # Usuario ingresa 1..N; restamos 1 para 0-based
                concesionario.vender_auto(indice)  # Intenta vender el auto en la posición dada

        elif opcion == "3":  # MOSTRAR AUTOS
            concesionario.mostrar_autos()  # Muestra la lista de autos

        elif opcion == "4":  # DAR MANTENIMIENTO
            concesionario.mostrar_autos()  # Muestra la lista de autos para elegir
            if concesionario.autos:  # Si hay autos
                indice = int(input("Ingrese el índice del auto para dar mantenimiento: "))- 1  # Convertir a 0-based
                concesionario.dar_mantenimiento(indice)  # Llama al método que ejecuta mantenimiento

        elif opcion == "5":  # SALIR
            print("Saliendo del programa...")
            break  # Rompe el bucle principal y termina el programa
        else:  # Opción inválida en el menú principal
            print("Opción inválida, intente de nuevo.")

# Punto de entrada: si ejecutas este archivo directamente, se corre el menú.
if __name__ == "__main__":
    menu()
