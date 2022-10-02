# Escreva a função n_primos que recebe como argumento um número inteiro
# maior ou igual a 2 como parâmetro e devolve a quantidade de números
# primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def n_primos(n):
    quant_primos = 0
    for y in range(n, 1, -1):   # range(incio, fim, passo)
        if primo(y):
            quant_primos += 1
    return quant_primos

def primo(x):
    i = 1
    cont = quant_primos = 0
    while i <= x:
        if x % i == 0:
            cont = cont + 1      # se a divisão for igual a zero, adiciona 1 em cont, que será = ou > 2. Quando o numero for divisivel por pois (exceto o numero 2), cont sera igual ou maior que 3        i = i + 1
        i = i + 1
        if cont > 2:
            return False
    return True

