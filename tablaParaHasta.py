print("Ingrese cantidad de numeros: ")

while True:
    cantidadNum = int(input())
    if cantidadNum > 0:
        break

for num in range(1, cantidadNum + 1):
    print(num, " ", num * num, " ", num + num * num, sep="")
