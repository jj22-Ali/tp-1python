"""15. Crea un programa que escriba los números del 1 al 300, e indique cuáles son múltiplos de 5 y de 7. Cada 6 líneas debe mostrar una línea horizontal. Ejemplo:"""
cont = 1

while cont <= 300:
    if cont % 5 == 0:
        print(cont, " es multiplo de 5")
    elif cont % 7 == 0:
        print(cont, " es multiplo de 7")
    elif cont % 6 == 0:
        print("---------------------")
        print(cont)
    else:
        print(cont)

    cont += 1