# Escreva a função remove_repetidos que recebe como parâmetro uma lista
# com números inteiros, verifica se tal lista possui elementos repetidos
#e os remove. A função deve devolver uma lista correspondente à primeira
# lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

def soma_elementos(lista):
    soma=0
    for i in lista:
        soma = soma + i
    return soma


lista = [2,5,2,8]
soma = soma_elementos(lista)
print(soma)
