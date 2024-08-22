"""8.	Escribe un programa que pida un número y nos diga si es divisible por 4, 6, 8, o 10."""

nro = int(input("Ingrese un numero: "))

if nro % 4 == 0 : 
    print(nro, " es divisible por 4")
elif nro % 6 == 0 : 
    print(nro, " es divisble por 6")
elif nro % 8 == 0 : 
    print(nro, " es divisble por 8")
elif nro % 10 == 0 : 
    print(nro, " es divisble por 10")
else:
    print("no es divisible en ninguno")