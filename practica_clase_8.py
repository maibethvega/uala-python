"""Practica Clase 8 - 09/06/2022"""

"""Generar una clase alumnos que pida en el constructor algunos datos de los mismos, 
algunos atributos obligatorios son nombre, notas, el cual será un array con al menos 5 valores 
y desviación estándar"""

class Alumno:
    cont = 0
    alumnos = []

    def __init__(self, name, dni, materia, nota1, nota2,nota3, nota4, nota5):
        self.name = name
        self.dni = dni
        self.materia = materia
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5
        Alumno.cont += 1
        Alumno.alumnos.append(self)

    def dar_info(self):
        return f'Nombre: {self.name}\nDNI: {self.dni}\nMateria: {self.materia}\nNota1: {self.nota1}\nNota2: {self.nota2}\nNota3: {self.nota3}\nNota4: {self.nota4}\nNota5: {self.nota5}'

    @staticmethod
    def contar_alumnos():
        return len(Alumno.alumnos)

def promedio_nota(nota1, nota2, nota3, nota4, nota5):
        suma_nota = nota1 + nota2 + nota3 + nota4 + nota5
        return suma_nota / 5

alum1 = Alumno("Maibeth", 19090953, "Ingles", 7, 6, 8, 10, 5)
alum2 = Alumno("Leonel", 38470822, "Ingles", 9, 10, 10, 6, 8)
alum3 = Alumno("Noe", 95784587, "Ingles", 4, 3, 5, 7, 4)
alum4 = Alumno("Marfre", 95784587, "Ingles", 10, 7, 4, 3, 5)
alum5 = Alumno("Mario", 95784587, "Ingles", 5, 9, 7, 7, 4)

print("Datos de los Alumnos")
print(alum1.dar_info())
print("Promedio de las Notas: " + str(promedio_nota(alum1.nota1, alum1.nota2, alum1.nota3, alum1.nota4, alum1.nota5)))
print("")
print(alum2.dar_info())
print("Promedio de las Notas: " + str(promedio_nota(alum2.nota1, alum2.nota2, alum2.nota3, alum2.nota4, alum2.nota5)))
print("")
print(alum3.dar_info())
print("Promedio de las Notas: " + str(promedio_nota(alum3.nota1, alum3.nota2, alum3.nota3, alum3.nota4, alum3.nota5)))
print("")
print(alum4.dar_info())
print("Promedio de las Notas: " + str(promedio_nota(alum4.nota1, alum4.nota2, alum4.nota3, alum4.nota4, alum4.nota5)))
print("")
print(alum5.dar_info())
print("Promedio de las Notas: " + str(promedio_nota(alum5.nota1, alum5.nota2, alum5.nota3, alum5.nota4, alum5.nota5)))


print("hola")



"""
print(a.cont)
print(b.cont)
print(Persona.contar_personas())
print(a.contar_personas())"""
