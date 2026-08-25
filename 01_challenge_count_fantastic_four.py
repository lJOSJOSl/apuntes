'''
¿Esta en equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantasticos, la union y el equilibrio entre los
poderes es fundamental para enfrentar cualquier desafio. En este
problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:
Crea una función en Python que reciba una cadena de texto. Esta funcion
debe contar cuantas veces aparece la letra R (para Reed Richards) y
cuantas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la
alianza entre la mente y el fuego esta en equilibrio y la funcion debe
retornar True.
- Si las cantidades no son iguales, la funcion debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena,
se entiende que el equilibrio se mantiene (0 = 0), por lo que la funcion
debe retornar True.
'''
import os
os.system("cls")

def equilibrio_alianza(texto):
    '''Ejercicio que cuenta la cantidad de R y J que hay en un texto
        Fue realizado sin ayuda con el conocimiento adquirido a traves
        de los apuntes.
    '''
    texto = texto.lower()
    contador_Rs = 0
    contador_Js = 0
    for i in texto:
        if i == "r":
            contador_Rs += 1
        if i == "j":
            contador_Js += 1
    if contador_Rs > contador_Js:
        return False
    elif contador_Js > contador_Rs:
        return False
    else:
        return True

#print(equilibrio_alianza("rodrigo"))

def check_is_balanced(text):

    text = text.upper()

    # Contar facilmente alguna letra en un texto.
    
    count_r = text.count("R") # Reed richards
    count_j = text.count("J") # Johnny Storm

    print(f"count_r: {count_r} count_j: {count_j}")

    #if count_r == count_j:
    #    return True
    #else:
    #   return False

    return count_r == count_j

print(check_is_balanced("RRJJ"))
print(check_is_balanced("RRJJJ"))
print(check_is_balanced("RRRRJJ"))
print(check_is_balanced(""))