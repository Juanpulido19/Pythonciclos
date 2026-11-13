print("Escriba su numerito")
n = int(input())

if n > 0:
    copiaNumero = n
    contadorCifras = 0
    sumaCifras = 0
    while copiaNumero > 0:
        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        sumaCifras = sumaCifras + cifra
        contadorCifras = contadorCifras + 1

    print("La cantidad de cifras de  ", n, sep="")
    print("son:", contadorCifras, sep="")
    print("La sumatoria es:", sumaCifras, sep="")
else:
    print(" No es un numero positivo")
