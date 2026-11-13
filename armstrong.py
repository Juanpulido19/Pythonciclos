print("Escriba su numero, para ver si es Armstrong")
n = int(input())

copiaNumero = n
contadorCifras = 0
sumaCifras = 0
while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    sumaCifras = sumaCifras + cifra
    contadorCifras = contadorCifras + 1

print("La cantidad de cifras de  ", n, sep="")
sumaCifras = 0
copiaNumero = n
while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    sumaCifras = sumaCifras + (cifra ** contadorCifras)

print("son:", contadorCifras, sep="")
if n == sumaCifras:
    print("Es un numero amstrong")
else:
    print("No es un numero amstrong")
