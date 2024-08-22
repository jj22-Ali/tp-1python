"""12.	Escribe un programa que pida una calificación (número). Muestra la evaluación según la calificación:
●	0-2: Muy Malo
●	3-4: Malo
●	5-6: Regular
●	7-8: Muy Bueno
●	9-10: Excelente
"""

nro = int(input("Ingresa una nota: "))

if(nro > 0 and nro <= 2):
    print("nota: Muy Mala")
elif(nro >= 3 and nro <= 4):
    print("nota: Malo")
elif(nro >= 5 and nro <= 6):
    print("nota: Regular")
elif(nro >= 7 and nro <= 8):
    print("nota: Muy Bueno")
elif(nro >= 9 and nro <= 10):
    print("nota: Excelente")
else:
    print("Ingrese un numero entre 0-10")