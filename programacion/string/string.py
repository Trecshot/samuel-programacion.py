# STRING

mi_first_string  = "mi string con comillas dobles"
mi_second_string  = 'mi string con comillas simples'

print(mi_first_string, mi_second_string)
print(f'esto es un texto de una variable ' + mi_first_string + '  ' + mi_second_string) 
print(f'esto es un texto{mi_first_string}xdxdxd')

other_string = 'hola'

a,b,c,d =other_string

#print(c )#se refiere a la letra de la palabra hola como es la tercer letrea entonces es l

print(a)
print(b)
print(c)
print(d)

print(f'{a}{b}{c}{d}')

print(mi_first_string.upper()) #UPPER hace que todo el texto este en mayuscula
print(mi_first_string.capitalize()) # CAPITALIZE lo que hace poner solo la primera letra en mayuscula
print(mi_first_string.lower())# LOWER pone todo en minusculas
print(len(mi_first_string))# LEN cuenta la cantidad de caracteres que tiene la variable
print(mi_first_string.find('r')) # FIND la posicion en la que esta en la variable pero no exacto menos uno
print(mi_first_string.count('l')) # countt ES LA CANTIDAD DE VECES QUE ESTA ESTA ESA LETRA EN LA VARIABLE
print(mi_first_string.lower().isupper())# se puede hacer junto