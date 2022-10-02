# Enunciado: Dado um número inteiro n, n > 0, e um dígito d que 0 <= d <= 9,
# determinar quantas vezes d ocorre em n.

n = int(input("Entre com o número inteiro > 0: "))
d = int(input("Entre com o número digito (de 0 a 9): "))

conta_digito=0
n_salvo = n
while n > 0:
    dig = n % 10
    n = n // 10
    if dig == d:
        conta_digito = conta_digito + 1

print("O digito", d, "ocorre", conta_digito, "vezes em ", n_salvo)
