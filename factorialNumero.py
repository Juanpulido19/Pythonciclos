print("Ingrese el numero para el factorial: ")
n = int(input())

if n < 0:
    print("No se puede calcular el factorial")
else:
    factorial = 1
    inferiores = 1

    while inferiores <= n:
        factorial = factorial * inferiores
        inferiores = inferiores + 1

    print("Factorial de ", n, " es: ", factorial, sep="")
