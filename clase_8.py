"""Clase 8 - 09/06/2022"""

class Persona:
    nacionalidad = 'Terrestre'
    cont = 0
    personas = []

    def __init__(self, name, dni):
        self.name = name
        self.dni = dni
        Persona.cont += 1
        Persona.personas.append(self)

    def dar_info(self):
        return f'Name: {self.name}\nDNI: {self.dni}'

    @staticmethod
    def contar_personas():
        return len(Persona.personas)

a = Persona("Maibeth", 19090953)
print(a.contar_personas())
b = Persona("Leonel", 38470822)
c = Persona("Noe", 95784587)

print(a.dar_info())
print(b.dar_info())
print(a.cont)
print(b.cont)
print(Persona.contar_personas())
