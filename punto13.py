"""13.	Realiza un programa que escriba una pirámide con asteriscos hasta un número dado por el usuario. Ejemplo para 5:"""
cont = 0

for cont in range(10):
    for x in range(cont + 1):
        print("*", end="")
    print(" ")