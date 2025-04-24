# LISTAS Y TUPLAS

my_list = ['python,', 53, False, 'hola mundo']
print(type(my_list))

print(my_list)
print(my_list[1])# en la programacion empieza a contr desde cero y su pones un -1 empieza en lo ultimo

my_list.append('55')# append sirve para agregar
print(my_list)

my_list.insert(1,'mamala')# insert casi igual que el append pero agrega en el lugar que tu quieras
print(my_list)

my_list.remove('hola mundo')# remove sirve para remover tu le escribes que es lo que quiera que remueva
print(my_list)

my_list.pop(1)# lo mismo pero enves de ponerlo con palabras es con numero
print(my_list)

#print(my_list.pop(1)) de vuelve lo ue borro 
#print(my_list)

print(my_list.count(53))#cuenta la cantidad de veces que esta el numero pero tomoa en cuenta si es int o str

my_list.pop(1)# lo mismo pero enves de ponerlo con palabras es con numero

my_list.reverse()# reverse cuenta la lista pero al reves
print(my_list)

my_list.clear()# clear borra toda la lista la deja vacia
print(my_list)