# Jogo NIM


def computador_escolhe_jogada(n,m):
    computador_retira = 1
    while (n - computador_retira) % (m + 1) != 0 and computador_retira <=m:
        computador_retira +=1
    print("O computador tirou", computador_retira, "peças.")      
    return computador_retira


def usuario_escolhe_jogada(n,m):
    numerovalido = False
    while not numerovalido:
        usuario_retira = int(input("Quantas peças você vai retirar? "))
        if usuario_retira > m or usuario_retira == 0:
            print("Oops! Jogada invalida! Tente de novo. ")
        else:
            numerovalido = True
    print("Você tirou", usuario_retira, "peças.")
    return usuario_retira


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("Você começa!")
        usuario_retira = usuario_escolhe_jogada(n,m)
        n -= usuario_retira
        vez = True              # True = vez do computador
    else:                       # Computador começa
        print("Computador começa!")
        computador_retira = computador_escolhe_jogada(n,m)
        n -= computador_retira
        vez = False
    print("Agora restam", n, "peças no tabuleiro")

    while n > 0:
        if vez == True:
            computador_retira = computador_escolhe_jogada(n,m)
            n -= computador_retira
            vez = False
        else:
            usuario_retira = usuario_escolhe_jogada(n,m)
            n -= usuario_retira
            vez = True
        if n > 0:
            print("Agora restam", n, "peças no tabuleiro")
        elif n == 0 and vez == False:    # False porque depois que o computador jogou, mudou para False
            vencedor = ("O computador")
        elif n == 0 and vez == True:
            vencedor = ("Você")
    return vencedor


def campeonato():
    i = 1
    computador = usuario = 0
    print("Você escolheu um campeonato!")
    for i in range (1,4,1):
        print("**** Rodada", i,"****")
        vencedor = partida()
        print("Fim de jogo!", vencedor, "ganhou!")
        if vencedor == ("O computador"):
            computador += 1
        elif vencedor == ("Você"):
            usuario += 1
    i += 1
    return (usuario,computador)


usuario = []
vencedor = []
print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato"))
if escolha ==1:
    vencedor = partida()
    print("Fim de jogo!", vencedor, "ganhou!")
if escolha ==2:
    resultado = campeonato()
    print("Placar: Você", resultado[0], "X", resultado[1], "Computador")


"""
Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"

Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.

O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.

Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.
"""
