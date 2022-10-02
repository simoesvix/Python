# Enunciado: Dados um número inteiro n, n > 0, e uma sequência com n números
# inteiros, determinar quantos números da sequência são pares e quantos são ímpares.

tamanho = int(input("Digite o tamanho da sequencia: "))
i = par = impar = 0
while i < tamanho:
    valor = int(input("Digite um número da sequência: "))
    if valor > 0 and valor%2==0:
        par += 1
        i += 1
    elif valor > 0 and valor%2>0:
        impar += 1
        i +=1
    elif valor < 0:
        i +=1
print("A sequência tem", par, "número(s) par(es) e", impar, "impar(es)")
