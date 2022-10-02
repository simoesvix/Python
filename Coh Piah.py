import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
  
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1    
    textos = []   
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")   
    while texto:   
        textos.append(texto)   
        i += 1  
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")  

    return textos



def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somaDiferencas = 0
    for traco in range(len(as_a)):
        somaDiferencas += abs(as_a[traco] - as_b[traco])
        #print(somaDiferencas)
    somaDiferencas = somaDiferencas / 6

    return somaDiferencas



def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    #print(sentencas)            

    # Formando uma lista de frases para cada sentença da lista de sentenças:
    listaDeFrases = []
    for item in sentencas:
        frases = separa_frases(item)
        #print(item)   
        for f in frases:
            listaDeFrases.append(f)
    #print(frases)              
    #print(listaDeFrases)       

    # Os comandos abaixo formam uma lista de palavras com as palavras de cada frase da sentença.
    listaDePalavras = []
    for ldf in listaDeFrases:
        palavrasSeparadas = separa_palavras(ldf)
        for palavras in palavrasSeparadas:
            listaDePalavras.append(palavras)
    #print(listaDePalavras)     

    # Cálculo das variáveis da assinatura do texto:
    # Tamanho médio das palavras  =  soma dos tamanhos das palavras / número total de palavras.
    somaTamanhoPalavras = 0
    quantidadePalavras = len(listaDePalavras)
    for palavra in listaDePalavras:
        somaTamanhoPalavras = somaTamanhoPalavras + len(palavra)
    tamanhoMedioPalavras = somaTamanhoPalavras/quantidadePalavras


    # Relação Type-Token = Número de palavras diferentes / número total de palavras.
    quantidadePalavrasDifer = n_palavras_diferentes(listaDePalavras)
    typeToken = quantidadePalavrasDifer / quantidadePalavras
    #print("Quantidade de palavras diferentes:", quantidadePalavrasDifer)    
    #print("Relação Type-Token: ", typeToken)                                

    # Razão Hapax Legomana = número de palavras que aparecem uma única vez / total de palavras.
    quantidadePalavrasUnicas = n_palavras_unicas(listaDePalavras)
    hapax = quantidadePalavrasUnicas / quantidadePalavras
    #print("Quantidade de palavras únicas:", quantidadePalavrasUnicas)   
    #print("Razão Hapax Legomana : ", hapax)                             

    # Tamanho médio da sentença = soma da quantidade de caracteres das sentenças / número de sentenças
    somaCaracterSentenca = 0
    for s in sentencas:
        somaCaracterSentenca = somaCaracterSentenca + len(s)
        #print(s)        
    tamanhoMedioSentenca = somaCaracterSentenca / len(sentencas)
    #print("Soma dos caracteres da sentença: ", somaCaracterSentenca)            
    #print("Tamanho da sentença: ", len(sentencas))                              
    #print("Tamanho médio da sentença: ", tamanhoMedioSentenca)                  
    
    # Complexidade de sentença = número total de frases / número de sentenças
    complexidade = len(listaDeFrases) / len(sentencas)
    #print("Complexidade: ", complexidade)          

    # Tamanho Médio de Frase = soma dos caracteres de cada frase / numero de frases do texto
    SomaCaracterFrase = 0
    for x in listaDeFrases:
        SomaCaracterFrase =  SomaCaracterFrase + len(x)
    tamanhoMedioFrase = SomaCaracterFrase / len(listaDeFrases)
    #print("Tamanho Médio de Frases: ", tamanhoMedioFrase)                       
    
    assinaturaDoTexto = [tamanhoMedioPalavras, typeToken,hapax, tamanhoMedioSentenca, complexidade, tamanhoMedioFrase]
    #print(assinaturaDoTexto)    

    return assinaturaDoTexto


def avalia_textos(texto, assinaturaRefer):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturasTextos = []
    for item in texto:
        assinaturasTextos.append(calcula_assinatura(item))       # Gera uma lista com as assinaturas dos textos a serem comparadas com a assinatura de referência
    #print(assinaturasTextos)

    comparacaoAssinaturas = []
    for assinatura in assinaturasTextos:                        # Compara as assinaturas dos textos com a assinatura de referência (digitada)
        comparacaoAssinaturas.append(compara_assinatura(assinaturaRefer, assinatura))
    #print(comparacaoAssinaturas)        

    provavelCohPiah = comparacaoAssinaturas[:]
    menorPontuacao = min(provavelCohPiah)
    #print("Menor Pontuacao", menorPontuacao)  
    index = provavelCohPiah.index(menorPontuacao) + 1 # A função devolve o índice do texto, que começa com zero. Por isso, para identificar o número do texto inseriro deve ser acrescido de +1.
    #print("Texto: ", texto[index])
    #print("Index: ", index)                   

    return index       


def main():
    assinaturaRefer = le_assinatura()       # Entra com a assinatura de referência
    #print(assinaturaRefer)        
    texto = le_textos()                     # Entra com os textos

    index = avalia_textos(texto, assinaturaRefer)
    print("O autor do texto", index, "está infectado com COH-PIAH.")

main()

