#-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasena_correcta = "contraseña"

while True:
    contrasena_ingresada = input("Ingresa la contraseña: ")
    if contrasena_ingresada == contrasena_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break  # Romper el bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")


