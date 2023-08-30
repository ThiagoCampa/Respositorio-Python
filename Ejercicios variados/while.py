cont=1
suma= 0

while cont <= 5:
    num= int(input("ingrese un numero:"))
    suma= suma + num #acumulamos, es equivalente a += num
    cont= cont + 1 

print("la suma es:", suma)
print("el promedio es:", suma/cont)