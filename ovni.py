T = int(input())
for t in range(T):
    linha = input().split(" ")
    linha2 = [int(e) for e in linha]
    raio1 = linha2[0] * 2
    raio2 = linha2[1] * 2
    plataforma = linha2[2] * 2
    if raio1 + raio2 <= plataforma:
        print("CABE!", end="" if t == T - 1 else "\n")
    else:
        print("NAO CABE!", end="" if t == T - 1 else "\n")


