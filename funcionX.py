print("Ingrese el mayor valor para x")
while True:
    valorX = int(input())
    if valorX >= 0:
        break

for x in range(0, valorX + 1, 2):
    funcionY = x ** 3 + x ** 2 - 5
    print("Para x=", x, " ", "F(x) = ", funcionY, sep="")
