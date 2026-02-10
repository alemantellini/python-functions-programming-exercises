#EJERCICIO 8 - Function parameters
# Your code goes here:
def render_person(name, date, color, age, gender):
    return f"{name} is a {age} years old {gender} born in {date} with {color} eyes"
# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
# Para insertar variables en un string en Python, 
# La forma más moderna y recomendada es usar f-strings (literales de cadena formateados), 
# anteponiendo una f a las comillas y colocando las variables entre llaves {}.
