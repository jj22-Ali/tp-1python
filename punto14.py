"""14. Haz un programa que escriba una pirámide inversa de asteriscos hasta un número dado por el usuario. Ejemplo para 4:"""

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(" ")