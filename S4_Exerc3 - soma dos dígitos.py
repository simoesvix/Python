# Escreva um programa que receba um número inteiro na entrada,
# calcule e imprima a soma dos dígitos deste número na saída

n =(input("Digite o número inteiro: "))
tamanho=len(n)
n = int(n)
i = soma = 0
while i < tamanho:
    soma = soma + n%10
    n = n//10
    i += 1
print(soma)
