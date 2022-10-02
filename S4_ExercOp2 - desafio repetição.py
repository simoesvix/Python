# Escreva um programa que receba um número inteiro na entrada e
# verifique se o número recebido possui ao menos um dígito com um
# dígito adjacente igual a ele. Caso exista, imprima "sim"; se não
# existir, imprima "não".

n =(input("Digite o número inteiro: "))
tamanho=len(n)
n = int(n)
i = n1 = 0
n2 = 1
while i < tamanho and n1!=n2:
    n1 = n%10
    n = n//10
    n2 = n%10
    if n1==n2:
        print("sim")
    i += 1
if n1!=n2:
    print("não")
