###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
os.system("cls")

print("Mi mensaje")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

print("\n Sentencia condicional con else")

edad=15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 40
if nota >= 90:
    print("¡Sobresaliente!")
elif nota >=70:
    print("Notable")
elif nota >=50:
    print("Aprobado")
else:
    print("No está calificado")

print("\n Condiciones múltiples")

edad = 16
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

if edad >= 18 and tiene_carnet:
    print("Puedes conducir🚗")
else:
    print("¡¡Policia🚓!!")


# un pueblo de Venezuela Isla Margarita
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Margarita")
else:
    print("¡Paga al policia y te deja conducir!")

es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
    print("¡JOS venga hay que trabajar!")

print("\n Anidar condicionales")
edad = 18
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la discoteca")

# Mas fácil
# if edad < 18:
#    print("No puedes entrar a la discoteca")
# elif tiene_dinero:
#    print("Puedes ir a la discoteca")
# else:
#    print("Quedate en casa")

numero = 5
if numero: #True
    print("El numero no es cero.")

numero = 0
if numero: #False
    print("Aqui no entrará nunca")

nombre = ""
if nombre:
    print("El nombre no es vacio")

nombre = " "
if nombre:
    print("El nombre no es vacio")

nombre = "Juan"
if nombre:
    print("El nombre no es vacio")

numero = 3 # Asignacion
es_el_tres = numero == 3 #Comparacion
if es_el_tres:
    print("El numero es 3.")



print("\n La condicion ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición if [condición] else [codigo si no cumple]]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)