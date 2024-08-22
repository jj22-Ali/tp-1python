"""5.	Escribe un programa que solicite tres números y luego indique cuál es el menor."""

x = 0
resultado = 1000
for cont in range(3):
    nro = int(input("Ingrese un numero: "))
    print("intento ", cont)
    print("El numero ingresado es: ", nro)
    if nro < resultado:
        resultado = nro

print(" ")
print("El numero menor es ", resultado)