"""10.	Escribir un programa que muestre todos los múltiplos de 3 menores a un número dado"""

nro = int(input("Ingrese cualquier numero: "))
cont = 1

while cont <= nro:
    if cont % 3 == 0:
        print(cont, " es multiplo de 3")
    else:
        print(cont)
    cont += 1