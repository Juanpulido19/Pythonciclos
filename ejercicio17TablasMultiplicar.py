aciertos = 0

print("Ingrese la tabla que desea repasar (1 al 20):")
tabla = int(input())

for fila in range(1, 11):
    print(tabla, " x ", fila, " = ", sep="")
    respuesta = int(input())

    if respuesta == tabla * fila:
        print("¡Correcto! Muy bien")
        aciertos = aciertos + 1
    else:
        print("Incorrecto, el resultado es: ", tabla * fila, sep="")

print("Cantidad de respuestas correctas: ", aciertos, sep="")

if aciertos <= 5:
    print("Valoracion: Insuficiente")
else:
    if aciertos <= 7:
        print("Valoracion: Aceptable")
    else:
        if aciertos <= 9:
            print("Valoracion: Sobresaliente")
        else:
            print("Valoracion: Excelente")
