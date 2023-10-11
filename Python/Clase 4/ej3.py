#3-Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.

num= float(input("ingrese su numero: "))

if num > 0:
    print("El numero ingreado es positivo.")
elif num < 0:
    print("El numero ingresado en negativo.")
else:
    print("El numero es 0.")
