1# el usuario debera ingresar el valor de T°.
#celcius, farenheint, kelvin

def convertidor_temp(temperatura,inicio,final):
    resultado = ""
    print(resultado)
   # convercion de datos

temp = float (input("ingrese su temperatura a convertir"))
escala_inicial = input("inidque escala inicial: C, F o K")
escala_final = input("inidque escala final: C, F o K")

convertidor_temp(temp,temperatura_inicial,temperatura_final)#se le llama a la funcion


def convertidor_temp(temperatura,inicio,fin):
    resultado = 0
    
    if inicio == "K" :
        if fin =="C":
           pass
      elif fin =="F":
           pass
      else:
           print("escala final erronea")
     elif inicio == "C":
       if fin == "K":
          pass
     elif fin == "F":
          pass
    else:
         print("escala final erronea")
    elif inicio == "F":
       if fin =="K":
          pass
    elif fin == "C":
         pass
    else:
        print("escala final erroena")
    else: 
        print