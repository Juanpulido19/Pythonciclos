print("ingrese estudiantes")
cantidadDeEstudiantes = float(input())

apro = 0
repro = 0
contadorEstudiantes = 0
notaSumada = 0
while contadorEstudiantes < cantidadDeEstudiantes:
    contadorEstudiantes = contadorEstudiantes + 1
    print(" Ponga una nota")
    notaDeEstudiante = float(input())
    if notaDeEstudiante >= 3.0:
        apro = apro + 1
    else:
        if notaDeEstudiante <= 3.0:
            repro = repro + 1
    notaSumada = notaSumada + notaDeEstudiante

promedio = notaSumada / cantidadDeEstudiantes
print(" Su promedio es:", promedio, sep="")
print(" Cantidad de aprovados:", apro, sep="")
print("Cantidad de reprovados:", repro, sep="")
