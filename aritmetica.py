x = int(input())
simb = input()
y = int(input())
simb2 = input()
z = int(input())
ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: (x//y))}
try:
    if (simb == "+" or simb== "-") and (not simb2=="*" and not simb2=="/"):
        a = ops[simb](x,y)
        b = ops[simb2](a,z)
    elif (simb == "+") and (simb2=="*" or simb2=="/"):
        a = ops[simb2](y,z)
        b = ops[simb](x,a)
    elif (simb == "-") and (simb2=="*" or simb2=="/"):
        a = ops[simb2](y,z)
        b = ops[simb](x,a)
    else:
        a = ops[simb](x,y)
        b = ops[simb2](a,z)

    print(int(b), end="")
except:
    print("erro", end="")