suma= 0

for i in range(5):
    num= int(input("ingrese un numero: "))
    suma= suma + num #acumulamos, es quivalente suma += num

print("la suma es:", suma)
print("el promedio es:", suma/i+1)