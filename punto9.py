"""9.	Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (puede ser divisible por varios)."""

nro = int(input("Ingrese un numero: "))

if nro % 4 == 0 : 
    print(nro, " es divisible por 4")
if nro % 6 == 0 : 
    print(nro, " es divisble por 6")
if nro % 8 == 0 : 
    print(nro, " es divisble por 8")
if nro % 10 == 0 : 
    print(nro, " es divisble por 10")
else:
    print("no es divisible en ninguno")