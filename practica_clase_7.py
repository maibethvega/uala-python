"""Crear un método para el promedio y la suma"""
print("Inicio Función Suma")
def suma (a, b):
    print("Num1: " + str(a))
    print("Num2: " + str(b))
    return a + b

suma = suma(15, 85)
print("La suma es: " + str(suma))

print("Fin Función Suma")
print("")

print("Inicio Función Promedio")
def promedio (num1, num2, num3, num4, num5):
    print("Num1: " + str(num1))
    print("Num2: " + str(num2))
    print("Num3: " + str(num3))
    print("Num4: " + str(num4))
    print("Num5: " + str(num5))
    sumaNum = num1+num2+num3+num4+num5
    return sumaNum/5

promedio = promedio(15, 10, 20, 20, 20)
print("El promedio es: " +str(promedio))

print("Fin Función Promedio")
print("")

"""Iterar a través de un array y que muestre el promedio de los datos (mínimo 10 elementos)"""
print("Inicio ejercicio array")
un_array_10 = [10, 12, 15, 18, 19,20, 20, 20, 20, 13]
print(un_array_10)
sumaArray = 0
for x in un_array_10:
    x += 0
    sumaArray = sumaArray + x
    promedioArray = sumaArray / len(un_array_10)
    print(x)

print("La suma del arreglo es: " + str(sumaArray))
print("El promedio del arreglo es: " + str(promedioArray))


print("Fin ejercicio array")
print("")