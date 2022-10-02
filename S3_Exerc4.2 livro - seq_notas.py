# Enunciado: Dados um número inteiro n, n > 0, e uma sequência com n notas
# finais, determinar quantos alunos:

n = int(input("Digite a quantidade de alunos: "))
i=reprovado=recuperacao=aprovado=desem_mb=0
while i < n:
    nota = int(input("Digite a nota do aluno (de 0 a 10): "))
    if nota < 3:
        reprovado += 1
        i +=1
    elif nota >= 3 and nota <5:
        recuperacao +=1
        i +=1
    elif nota >= 5:
        aprovado +=1
        if nota > 8:
            desem_mb +=1
        i +=1

print("Total de alunos: ",n)
print("Alunos reprovados: ", reprovado)
print("Alunos de recuperação: ", recuperacao)
print("Alunos aprovados: ", aprovado)
print("Alunos com desempenho muito bom: ", desem_mb)
