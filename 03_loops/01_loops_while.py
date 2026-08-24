###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condición. 
###

import os
os.system("cls")

print("\n Bucle while:")

# Bucle con una simple condicion
contador = 0

while contador < 5:
    print(contador)
    contador += 1 # Es super importante para evitar un bucle infinito

# Utilizando la palabra break
while True:
    print("Hola")
    break

print("\n Bucle while con break:")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # sale del bucle

contador = 0

while contador <= 100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        print("El numero es multiplo de 5")
        break

# continue, que lo hace es saltar esa iteracion en concreto
# y continuar con el bucle
print("\n Bucle continue")

contador = 0

while contador <10:
    contador += 1
    if contador % 2 == 0:
        continue
    # 👇
    print(contador)

# else, que se ejecuta si no se cumple la funcion
print("\n Bucle while con else")
contador = 0
while contador < 5:
    print(contador)
    contador +=1
else:
    print("El bucle ha terminado")

# else, que se ejecuta si no se cumple la funcion
contador = 0
while contador < 5:
    print(contador)
    contador +=1
    break
else:
    print("El bucle ha terminado")
    # else, que se ejecuta si no se cumple la funcion
contador = 0
while contador < 5:
    print(contador)
    contador +=1
    break
print("El bucle ha terminado")

# pedirle al usuario un numero que tiene que ser positivo,
# si no, no le dejamos en paz

numero = -1
while numero <= 0:
    numero = int(input("Escribe un numero positivo: "))

print(f"El numero que has introducido es {numero}")

numero = -1

while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
        if numero < 0:
            print("El numero debe ser positivo. Trata de nuevo")
    except:
        print("Debes de ingresar un numero")

print(f"El numero que has introducido es {numero}")