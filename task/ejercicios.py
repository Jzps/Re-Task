#Ejercicio 1 Estudiante universitario
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.promedio = 0.0
        self.materias_inscritas = []

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años, estudio {self.carrera}."

    def agregar_materias(self, materia):
        if materia not in self.materias_inscritas:
            self.materias_inscritas.append(materia)
            return f"{self.nombre} se ha inscrito en {materia}"
        else:
            return f"{self.nombre} ya está inscrito en {materia}"

    def agregar_nota(self, materia, nota):
        if materia in self.materias_inscritas and 0.0 <= nota <= 5.0:
            if self.promedio == 0.0:
                self.promedio = nota
            else:
                total_materias = len(self.materias_inscritas)
                suma_actual = self.promedio * (total_materias - 1)
                self.promedio = (suma_actual + nota) / total_materias
            return f"Nota {nota} agregada a {materia}. Nuevo promedio: {self.promedio:.2f}"
        else:
            return f"Error: materia no inscrita o nota inválida"

#input
nombre = input("ingrese su nombre:")
edad = input("ingrese su edad:")
carrera = input("ingrese su carrera:")

est = Estudiante(nombre, edad, carrera)
print(est.presentarse())

materia = input("ingrese materia a inscribir:")
print(est.agregar_materias(materia))

nota = float(input(f"ingrese la nota para la {materia}: "))
print(est.agregar_nota(materia, nota))

#Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
        else:
            raise ValueError("La base y la altura deben ser valores positivos")
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def es_cuadrado(self):
        if self.base == self.altura:
            return "Sí, es un cuadrado"
        else:
            return "No, es un rectángulo"
        
    def mostrar_info(self):
        return f"""
    INFORMACIÓN DEL RECTÁNGULO
    Base: {self.base} unidades
    Altura: {self.altura} unidades
    Área: {self.calcular_area():.2f} unidades²
    Perímetro: {self.calcular_perimetro():.2f} unidades
    ¿Es cuadrado?: {self.es_cuadrado()}
        """

#main
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
rec = Rectangulo(base, altura)

while True:
    print("\n--- MENÚ ---")
    print("1. Calcular área")
    print("2. Calcular perímetro")
    print("3. Verificar si es cuadrado")
    print("4. Mostrar toda la información")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Área: {rec.calcular_area():.2f}")
    elif opcion == "2":
        print(f"Perímetro: {rec.calcular_perimetro():.2f}")
    elif opcion == "3":
        if rec.es_cuadrado():
            print("Sí es cuadrado")
        else:
            print("No es cuadrado")
    elif opcion == "4":
        print(rec.mostrar_info())
    elif opcion == "5":
        print("Saliendo del programa... 👋")
        break
    else:
        print("Opción inválida, intente de nuevo.")
