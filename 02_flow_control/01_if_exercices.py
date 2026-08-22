###
# Ejercicios
###

import os
os.system("cls")

# Ejercicio 1: Determinar el mayor de dos numeros
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cual es mayor o si son iguales

a = int(input("Ingresa un numero: "))
b = int(input("\nIngresa un numero: "))

if a == b:
    print(f"\nLos numeros a = {a} y b = {b} son iguales.")
elif a > b:
    print(f"\nEl numero a = {a} es mayor que b = {b}")
else:
    print(f"\nEl numero b = {b} es mayor que a = {a}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos numeros y una operacion (+, -, *, /)
# Realiza la operacion y muestra el resultado (Maneja la division entre zero)

a = int(input("\nIngresa un numero: "))
b = int(input("\nIngresa un numero: "))
operador = input(
"\nSuma: +"
"\nResta: -"
"\nMultiplicacion: *"
"\nDivision: /"
"\nIngresa el operador: "
)

if operador == "+":
    print(a + b)
elif operador == "-":
    print(a - b)
elif operador == "*":
    print(a * b)
elif operador == "/":
    if b==0:
        print("Error no se puede dividir entre 0")
    else:
        print(a/b)


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, exceptop si es divisible por 100
# pero no por 400.

a = int(input("Ingresa un año: "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print("\nEl año es bisiesto")
else:
    print("\nEl año no es bisiesto")

# Ejercicio 4: Categorizar por edades
# Pide al usuario que introduza una edad y la clasique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o mas)

edad = int(input("\nIngresa una edad: "))

if edad <= 2:
    print("\nEres un bebé")
elif edad <= 12:
    print("\nEres un niño")
elif edad <= 17:
    print("\nEres un adolescente")
elif edad <= 64:
    print("\nEres un adulto")
else:
    print("\nEres un adulto mayor")