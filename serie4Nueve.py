print("Ingrese la cantidad de terminos a generar")
cantidadTerminos = int(input())

contadorNumeros = 0
termino = 1
while True:
    print(termino, ",", sep="")
    termino = termino + 2
    contadorNumeros = contadorNumeros + 1
    if contadorNumeros >= cantidadTerminos - 1:
        break

print(termino)
