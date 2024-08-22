"""11.	Escribir un programa que nos diga si un número dado es perfecto (un número perfecto es igual a la suma de sus divisores propios, excluyendo el número mismo)."""

nro = int(input("Ingrese cualquier numero: "))
cont = 1
suma = 0
while cont < nro:
    if nro % cont == 0:
        print(cont)
        suma = suma + cont
    cont += 1
if nro == suma:
    print("El resulatado de los divisores: ", suma)
    print("El ", nro, " es un numero perfecto")
else: 
        print("El ", nro, " no es un numero perfecto")

