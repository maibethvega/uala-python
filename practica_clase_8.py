"""Practica Clase 8 - 09/06/2022"""

"""Generar una clase alumnos que pida en el constructor algunos datos de los mismos, 
algunos atributos obligatorios son nombre, notas, el cual será un array con al menos 5 valores y desviación estándar"""

class Alumno:
    cont = 0
    alumnos = []

    def __init__(self, name, dni, materia, notas):
        self.name = name
        self.dni = dni
        self.materia = materia
        self.notas = notas
        Alumno.cont += 1
        Alumno.alumnos.append(self)

    def dar_info(self):
        return f'Nombre: {self.name}\nDNI: {self.dni}\nMateria: {self.materia}\nNotas: {self.notas}'

    @staticmethod
    def contar_alumnos():
        return len(Alumno.alumnos)

"""2.- Que haya un array en dicha clase que contenga a todos los alumnos que se van creando
3.- Generar método realice el promedio de las notas"""
def promedio_nota(notas):
    sumaNotas = 0
    for x in notas:
        x += 0
        sumaNotas = sumaNotas + x
        promedio_nota = sumaNotas / len(notas)
    print("Promedio de las notas: " + str(promedio_nota))


"""4.- Generar método traiga la nota más alta"""
def mayor_nota(notas):
    print("La Mayor nota es: " + str(max(notas)))


"""5 Generar método que elija al estudiante con mejor promedio, en caso de empate al que tenga menor desviación"""
def mejor_promedio(notas):
    print("El mejor promedio es: " + str(max(promedio_nota(notas))))


"""Alumnos"""
alum1 = Alumno("Maibeth", 19090953, "Ingles", [7, 6, 8, 9, 5])
alum2 = Alumno("Leonel", 38470822, "Ingles", [9, 10, 7, 6, 8])
alum3 = Alumno("Noe", 95784587, "Ingles", [4, 3, 5, 7, 4])
alum4 = Alumno("Marfre", 96784587, "Ingles", [8, 7, 4, 3, 5])
alum5 = Alumno("Mario", 33478956, "Ingles", [10, 10, 10, 10, 10])

print("Datos de los Alumnos:")
print(alum1.dar_info())
promedio_nota(alum1.notas)
mayor_nota(alum1.notas)
print("")
print(alum2.dar_info())
promedio_nota(alum2.notas)
mayor_nota(alum2.notas)
print("")
print(alum3.dar_info())
promedio_nota(alum3.notas)
mayor_nota(alum3.notas)
print("")
print(alum4.dar_info())
promedio_nota(alum4.notas)
mayor_nota(alum4.notas)
print("")
print(alum5.dar_info())
promedio_nota(alum5.notas)
mayor_nota(alum5.notas)
print("")
