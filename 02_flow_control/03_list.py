###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos
###
import os
os.system("cls")
# Creación de listas
print("\nCrear listas:")
lista1 = [1, 2, 3, 4, 5, 6] # lista de enteros
lista2 = ["manzanas", "peras", "platanos", "sandias"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2, 3], [4, "calcetin", 6], [7, 8, 9]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indice
print("\nAcceso a elementos por indice:")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # sandias
print(lista2[-2]) # platanos
print(lista2[-3]) # peras

print(lista_de_listas[1][1])

# Slicing (rebanado) de listas
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3])  # [1, 2, 3]
print(lista1[3:])  # [4, 5, 6]
print(lista1[:])   # [1, 2, 3, 4, 5, 6]

# Hay mas magia
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::-1])                 # Voltear lista
print(lista1[::2])                   # Imprimir la lista de 3 en 3
print(lista1[::2])                   # Imprimir la lista de 3 en 3      
#print(lista1[desde:hasta:paso]) #[desde:hasta:paso] 

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# Forma larga y menos eficiente
lista1 = lista1 + [4, 5 , 6]
print(lista1)

# Forma corta y mas eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de unalista
print("Longitud de la lista", len(lista1))