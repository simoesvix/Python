# Escreva a função maior_primo que recebe um número inteiro maior
# ou igual a 2 como parâmetro e devolve o maior número primo menor
# ou igual ao número passado à função

def maior_primo(n):
    for y in range(n, 1, -1):   # range(incio, fim, passo)
        if primo(y):
            return y

def primo(x):
    i = 1
    cont = 0
    while i <= x:
        if x % i == 0:
            cont = cont + 1      # se a divisão for igual a zero, adiciona 1 em cont, que será = ou > 2. Quando o numero for divisivel por pois (exceto o numero 2), cont sera igual ou maior que 3        i = i + 1
        i = i + 1
        if cont > 2:
            return False
    return True
