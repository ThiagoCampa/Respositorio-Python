#10-Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

"""num= int(input("Ingresa un número entero positivo: "))

if num <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Generar la cuenta atrás desde el número ingresado hasta 0
    countdown = ", ".join(str(i) for i in range(num, -1, -1))
    print(countdown)"""

"""numero= int(input("Ingrese un numero positivo:"))
while numero<0:
    print("No puede ingresar numeros negativos")
    numero= int(input("Ingrese un numero positivo:"))

for i in range(numero,-1,-1):
    print(i, end=", ")"""


n= int(input("Ingrese un numero entero positivo: "))

for i in range(n,-1, -1):
    print(i, end=", ")