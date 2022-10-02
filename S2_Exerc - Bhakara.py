import math

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))

delta = b**2 - 4*a*c

if delta==0:
    raiz_1 = (- b + math.sqrt(delta)) / (2*a)
    print("Esta equeação possui uma raiz:", raiz_1)
else:
    if delta<0:
        print("Esta esquação não possui raiz real")
    else:
        raiz_1 = (- b + math.sqrt(delta)) / (2*a)
        raiz_2 = (- b - math.sqrt(delta)) / (2*a)
        print("A primeira raiz é: ", raiz_1)
        print("A segunda raiz é: ", raiz_2)



        
