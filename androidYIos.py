votosAndroid = 0
votosIos = 0

print("PLATAFORMAS DISPONIBLES")
print("[A]Android")
print("[i]OS")
print("Desea realizar un nuevo voto [S] [N]?: ")
seguir = input()

while seguir == "S" or seguir == "s":
    print("Digite su voto (A o I): ")
    voto = input()

    if voto == "A" or voto == "a":
        votosAndroid += 1
    else:
        if voto == "I" or voto == "i":
            votosIos = votosIos + 1
        else:
            print("Respuesta no valida")

    print("Desea registrar otro voto? [S/N]")
    seguir = input()

print("Votos Android: ", votosAndroid, sep="")
print("Votos iOS: ", votosIos, sep="")

if votosAndroid > votosIos:
    print("La plataforma ganadora es Android")
else:
    if votosIos > votosAndroid:
        print("La plataforma ganadora es iOS")
    else:
        print("Hay empate en la votacion")
