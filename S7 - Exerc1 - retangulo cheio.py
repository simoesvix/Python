
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
a = larg = 1
while a <= altura:
    while larg <= largura:
        print("#", end="")
        larg += 1
    a += 1
    print()
    larg = 1
    


