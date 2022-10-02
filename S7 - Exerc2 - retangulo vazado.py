
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
a = larg = 1
while a <= altura:
    while larg <= largura:
        if larg == 1 or larg == largura or a == 1 or a == altura:
            print("#", end="")
        elif a!=1 or a!=altura:
            print(" ", end="")
        larg += 1
    a += 1
    print()
    larg = 1
    


