###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")


print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

nombre = "JOS"

ciudad = "Apizaco"

print(f"{nombre}\n{ciudad}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
n = "12345"
n_int = int(n)
n_float = float("12345")
n_2 = 3.99
n_2_int = int(n_2)

print(n)
print(n_int)
print(n_float)
print(n_2)
print(n_2_int)

'''
¿Qué ocurre? Ignora todo lo que esta despues del punto
solo toma el valor antes del punto por eso imprime 3 al
convertirlo a entero
'''

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "JOS"

edad = 26

altura = 1.7


print(f"¡Hola, Me llamo {nombre}, tengo {edad} años y mido {altura} metros. ")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# solucion_1

x = 3.141569
x = round(x)
x = int(x/2)
print(f"Solucion_1: {x}")

# solucion_2

resultado = int(round(3.1416) / 2)
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("Solucion_2: División entera de PI redondeado entre 2:", resultado)

# solucion_3

result = (round(3.14159) // 2)
print("Solucion_3: Division entera de PI redondeado entre 2:", result)