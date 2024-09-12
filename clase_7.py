"""CLASE 7 - 07/06/2022"""

"""Ejemplo set"""
un_Set = {1, 2, 3}
print(un_Set)
un_Set.discard(3)
print(un_Set)
print("FIn prueba set")
print("")

"""Ejemplo tupla"""
print("Inicio Tupla")
un_tupla = (3, 14, 15, 29)
print(un_tupla[2])
print("Fin Tupla")
print("")

"""Ejemplo Diccionario"""
print("Inicio Diccionario")
un_dict = {"Hola": "Mundo", 1: "Soy un número", 2: "Nuevo", 3: [1, 2, 4]}
print(un_dict)
print(un_dict[1])
print("Fin diccionario")
print("")

"""Ejemplo array"""
un_array = [2, 1, [5, "3"], 1, 2, [0, "3"]]
dos_array = [2, 12, 13, 15]

print(un_array[1])
print(len(un_array))
print(un_array[-1])
print(un_array[0:3])
print("Fin array")
print("")


print("Ejemplo If")
if un_array[0] == 1:
    print("Hola")
elif un_array[1] == 0:
    print("Holis, soy un elif")
else:
    print("No cumpli condiciones")

print("FIN")
print("")

"""Ejemplo Booleanos"""

print(int(3) == 3)

boo = ("3" == 3) or (4 == 4)
print(boo)

print("Fin Booleanos")
print("")


"""Ejemplo bucles FOR"""
print(un_array)
for i in un_array:
    print(i)

print(dos_array)
for x in dos_array:
    x += 3
    print(x)

print("Fin for")
print("")

"""Ejemplo bucles while"""
cont = 0
while (cont  <= 10):
    cont += 2
    print("Mai")

print("Fin while")
print("")

"""Ejemplo funciones"""

def suma (a, b):
    print("Num1: " +str(a))
    print("Num2: " +str(b))
    return a+b

suma = suma(5, 5)
print("La suma es: " +str(suma))

print("Fin funciones")
print("")