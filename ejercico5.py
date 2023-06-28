#Cualquier año divisible por 4 es un año bisiesto: por ejemplo, 1988, 1992 y 1996 son años bisiestos.

def esbisiesto(ano):
    a = ano%4
#    print(a)
    if a == 0:
            print("Es Biciesto")
    else:
            print("No es biciesto")


ano = int(input("Ingrese un año para determinar si es biciesto:"))
esbisiesto(ano)
