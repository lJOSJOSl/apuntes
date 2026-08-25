###
# Ejercicios (funciones)
# se retoman ejercicios de los anteriores apuntes para crear funciones y parametros.
###

import os
os.system("cls")

# Ejercicio 1: Mayor de dos números
# Practica: parámetros + return.
# Crea una función mayor_de_dos(a, b) que reciba dos números y devuelva el mayor. Si son iguales, devuelve cualquiera de ellos.

print("\n Ejercicio 1:")

def mayor_de_dos(a, b):
    '''Calcula el numero mayor de dos variables'''
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return f"a y b son iguales"

print(mayor_de_dos(5, 8))

# Ejercicio 2: Calculadora
# Practica: varios parámetros + return + if/elif.
# Crea una función calcular(a, b, operacion) que realice +, -, * y /. Debe controlar la división entre cero.

print("\n Ejercicio 2:")

def calcular(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b != 0:
            return a / b
        else:
            return f"No se puede dividir entre 0"

print(calcular(3, 0, "/"))

# Ejercicio 3: Factorial
# Practica: función + parámetro + return + bucle.
# Crea una función factorial(numero) que reciba un número entero positivo y devuelva su factorial usando un while.

print("\n Ejercicio 3:")

def factorial(numero):
    contador = 1
    resultado = 1
    while numero > contador:
        resultado = resultado * (contador+1)
        contador += 1
    return resultado

print(factorial(6))

# Ejercicio 4: Número primo
# Practica: función + return + bucles anidados.
# Crea una función es_primo(numero) que reciba un número y devuelva True si es primo y False si no lo es.

print("\n Ejercicio 4:")

def es_primo(numero):
    contador = 2
    while numero > contador:
        if numero % contador == 0:
            return False
        contador += 1
    return True

print(es_primo(5))

# Ejercicio 5: Suma de una lista
# numeros = [10, 20, 30, 40, 50]
# Practica: recibir una lista + acumulador + return.
# Crea una función sumar_lista(numeros) que reciba una lista de números y devuelva la suma de todos sus elementos usando un for.

print("\n Ejercicio 5:")

a=[10, 20, 30, 40, 50]

def sumar_lista(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma

print(sumar_lista(a))

# Ejercicio 6: Encontrar el máximo
# Crea una función encontrar_maximo(numeros) que reciba una lista y devuelva el número más grande usando un for.

print("\n Ejercicio 6:")

a=[10, 20, 30, 75, 40, 50]

def encontrar_maximo(numeros):
    maximo = numeros[0]
    for i in numeros:
        if i > maximo:
            maximo = i
    return maximo

print(encontrar_maximo(a))

# Ejercicio 7: Filtrar palabras
# listas/list comprehension. Crea una función palabras_largas(palabras) que reciba una lista de palabras y devuelva una nueva
# lista 
# únicamente con las palabras que tengan más de 5 caracteres.

print("\n Ejercicio 7:")

cosas = ["casa", "naranja", "luna", "mandarina", "perro", "gato", "elefante"]

def palabras_largas(palabras):
    largas = [palabra for palabra in palabras if len(palabra) > 5]
    return largas

print(palabras_largas(cosas))

# Ejercicio 8: Contar palabras por letra
# Crea una función contar_por_letra(palabras, letra) que reciba una lista de palabras y una letra, y devuelva cuántas palabras
# comienzan con esa letra, sin distinguir mayúsculas de minúsculas.

print("\n Ejercicio 8:")

cosas = ["casa", "naranja", "luna", "mandarina", "perro", "gato", "elefante", "licuado", "lana"]

def contar_por_letra(lista, letra):
    contador = 0
    for i in lista:
        
        if i[0].lower() == letra.lower():
            contador += 1
    return contador

print(contar_por_letra(cosas, "L"))