# Escreva um programa que receba um número natural n na entrada
# e imprima  n! n! (fatorial) na saída.
n = int(input("Digite o valor de n: "))
i=1
fat=1
while i <= n:
    fat = fat * i  
    i += 1
print(fat)

