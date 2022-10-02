# Escreva a função vogal que recebe um único caractere como parâmetro
# e devolve True se ele for uma vogal e False se for uma consoante.


def vogal(caracter):
    result=False
    if caracter in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        result = True
    return result
