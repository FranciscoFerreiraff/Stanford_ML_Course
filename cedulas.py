notas = [100, 50, 20, 10, 5, 2, 1]
entrada = int(input())
for i in notas:
    ced = entrada//i
    if ced == 0:
        pass
    else:
        entrada = entrada - i*ced
    if i == 1:
        print(str(ced) + " nota(s) de R$ " + str(i), end="")
    else:
        print(str(ced) + " nota(s) de R$ " + str(i))
