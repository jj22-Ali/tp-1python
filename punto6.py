"""6.	Escribe un programa que pida cuatro números y muestre en la pantalla el menor de los cuatro."""

cont = 1
x = 100000
print("Ingrese 4 numeros")
print("")
while cont <= 4:
    print("Intento ", cont)
    nro = int(input("Ingrese un numero: "))
    if nro < x :
        x = nro
    cont += 1
print("")
print("El menor de los 4 es ", x)