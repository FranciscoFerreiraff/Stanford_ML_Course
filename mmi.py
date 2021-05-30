T = int(input())
for t in range(T):
    linha = input().split(" ")
    linha2 = [int(e) for e in linha]
    maximo = max(linha2)
    menor = min(linha2)
    if int(maximo) == int(menor):
        print(str(menor) + " " + str(maximo), end="" if t == T - 1 else "\n")
        print("S", end="" if t == T - 1 else "\n")
    else:
        print(str(menor) + " " + str(maximo), end="\n")
        print("N", end="" if t == T - 1 else "\n")

