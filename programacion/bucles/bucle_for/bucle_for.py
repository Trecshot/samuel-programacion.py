# usamos eel ciclo FOR para recorrer elementos de un grupo de datos
juegos = ["Dota 2","MK","Street fighter","Counter Strike","7Daystodie"]
numeros =[10,20,30,40,50]

for juego in juegos:
    print(juego)

for numero in numeros:
    resultado = numero * numero
    print(f"El resultado de multiplicar {numero} * {numero} = {resultado}")

print('hola' in 'hola amigos')


print()
for num in range(5):
    print(num)

print()
for num in range(5,16,5):
    print(num)
    


for elemnto in enumerate(numeros):
    indice = elemnto[0]
    valor = elemnto[1]
    print(f"El inidce es:{indice} y el valor es: {valor}")