###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sireven para almacenar datos relacionados
###

# ejempplo tipico de diccionario

import os
os.system("cls")

persona = {
    "nombre" : "JOSJOS",
    "edad" : 26,
    "es_estudiante" : True,
    "calificaciones" : [7,8,9],
    "socials" : {
        "twitter" : "@JOSJOS",
        "instagram" : "@JOSJOS",
        "facebook" : "JOSJOS"
    }
}
#para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][0])
print(persona["socials"]["facebook"])

# cambiar valores al acceder
persona["nombre"] = "JOS"
persona["calificaciones"][0] = 10

# elimar completamente una propiedad
del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name" : "JOS", "edad": 26}
b = {"name" : "STUART", "es_estudiante" : True}

a.update(b)
print(a)