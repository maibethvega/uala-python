#Practica Clase 8 - 09/06/2022"""

#Generar una clase alumnos que pida en el constructor algunos datos de los mismos,
# algunos atributos obligatorios son nombre, notas, el cual será un array con al menos 5 valores y desviación estándar

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
        self.promedio = self.promedio()
        self.mayor_nota = self.mayor_nota()

    def dar_info(self):
        return f'Nombre: {self.name}\nDNI: {self.dni}\nMateria: {self.materia}\nNotas: {self.notas}'

    @staticmethod
    def contar_alumnos():
        return len(Alumno.alumnos)

   #2.- Que haya un array en dicha clase que contenga a todos los alumnos que se van creando
   # 3.- Generar método realice el promedio de las notas"""
    def promedio(self):
        return sum(self.notas) / len(self.notas)

    #4.- Generar método traiga la nota más alta
    def mayor_nota(self):
        return max(self.notas)

    #5 Generar método que elija al estudiante con mejor promedio, en caso de empate al que tenga menor desviación"""



#Alumnos
alum1 = Alumno("Maibeth", 19090953, "Ingles", [7, 6, 8, 9, 5])
alum2 = Alumno("Leonel", 38470822, "Ingles", [9, 10, 7, 6, 8])
alum3 = Alumno("Noe", 95784587, "Ingles", [4, 3, 5, 7, 4])
alum4 = Alumno("Marfre", 96784587, "Ingles", [8, 7, 4, 3, 5])
alum5 = Alumno("Mario", 33478956, "Ingles", [10, 10, 10, 10, 10])

print("Datos de los Alumnos:")
print(alum1.dar_info())
print("Promedio de las notas: " + str(alum1.promedio))
print("La mayor nota es: " + str(alum1.mayor_nota))
print("")
print(alum2.dar_info())
print("Promedio de las notas: " + str(alum2.promedio))
print("La mayor nota es: " + str(alum2.mayor_nota))
print("")
print(alum3.dar_info())
print("Promedio de las notas: " + str(alum3.promedio))
print("La mayor nota es: " + str(alum3.mayor_nota))
print("")
print(alum4.dar_info())
print("Promedio de las notas: " + str(alum4.promedio))
print("La mayor nota es: " + str(alum4.mayor_nota))
print("")
print(alum5.dar_info())
print("Promedio de las notas: " + str(alum5.promedio))
print("La mayor nota es: " + str(alum5.mayor_nota))
print("")