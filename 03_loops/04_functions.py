###
# 04 - Funciones
# Bloques de codigo reutilizable y parametrizables para hacer tareas especificas
###

import os
os.system("cls")

''' Definicion de una funcion.

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la funcion
    # return valor_de_retorno # opcional\

'''

# Ejemplo de una funcion para imprimir en consola
# def saludar():
#     print("¡Hola!")

# Ejemplo de una funcion con parametro

# def saludar_a(nombre):
#     print(f"¡Hola {nombre}!")

# saludar_a("JOSJOS")
# saludar_a("Ronald")
# saludar_a("Messi")

# El parametro es lo que acepta la funcion
# El argumento es lo que se le pasa a la funcion

# Funciones con mas parrametros
# def sumar(a, b):
#     suma = a + b
#    return suma

# print(sumar(2, 3))

# Documentar las funciones con docstring
# def restar(a, b):
#     """Resta dos numeros y devuelve el resultado"""
#     return a - b
# print(restar.__doc__)
# help(restar)

# parametros por defecto
# def multiplicar(a, b=2):
#     return a * b

# print(multiplicar(2))

# Argumentos por clave
# def describir_persona(nombre, edad, sexo):
#     '''DESCRIBE A UNA PERSONA'''
#     print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# describir_persona("JOSJOS", 25, "perro")
# describir_persona("Ronaldo", 48, "futbolista")
# describir_persona("hombre", "jorge", 20)

# Argumentos por clave
# parametros nombrados
# describir_persona(sexo="perro", nombre="JOSJOS", edad=26)

# Argumentos de longitud de variable (*args):
# def sumar_numeros(*args):
#     suma = 0
#     for numero in args:
#        suma += numero
#     return suma
# print(sumar_numeros(1, 2, 3, 4, 5))
# print(sumar_numeros(1, 2))
# print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="JOSJOS", edad=25, sexo="perro")
print("\n")
mostrar_informacion_de(name="Madeval", edad=21, country="Chile")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

