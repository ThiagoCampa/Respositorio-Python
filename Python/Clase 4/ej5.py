#5-Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.

"""""a = 5
 
if(a>=1 and a<=10):
    print("Esta entre 1 y 10")
else:
    print("No esta en ese rango")"""


num = float(input("Ingresa un numero: "))

if 0 <= num <= 10:
    print("El número está entre 0 y 10")
else:
    print("El número no está entre 0 y 10")

