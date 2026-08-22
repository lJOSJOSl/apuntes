###
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asignar una variable
# Solo hace falta poner esto
# my_name = "JOS"
# print(my_name)

# age = 32
# print(age)

# age = 26
# print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecucion
# que no tienes que declararlo explicitamente

# name = "JOS"
# print(type(name))
# name = 32
# print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automaticas
# print(10 + "2") 

# f-strin(literal de cadena de formato)
# desde la version Python 3.6
# print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
# name, age, city = "JOS", 26, "Apizaco"

# Convenciones de nombres de variables
# mi_nombre_de_variable = "ok" #snake_case
# nombre = "ok"

# MiNombreDeVariable = "ko" #PascalCase
# minombredevariable = "ko" #todojunto

# mi_nombre_de_variable_123 = "ok"

# MI_CONSTANTE = 3.14 # UPPER_CASE > CONSTANTES

#nombres no válidos de variables
# 123123_variable = "ko"
# mi-variable = "ko"
# mi variable = "ko"

# True = False

# ["False", "None", "True", "and", "as", "assert",
#  "async", "await", "break", "class", "continue",
#  "def", "del", "elif", "else", "except", "finally",
#  "for", "from", "global", "if", "import", "in", "is",
#  "lambda", "nonlocal", "not", "or", "pass", "raise"
#  "return", "try", "while", "with", "yield"]

# types anotation
# is_user_logged_in: bool = True
# print(is_user_logged_in)

# is_user_logged_in = 42
# print(is_user_logged_in)