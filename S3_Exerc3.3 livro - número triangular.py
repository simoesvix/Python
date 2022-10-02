# Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos. 

print("Determina se um numero n é triangular")

# leia o valor de n
n = int(input("Digite o valor de n: "))

i = 1
while i * (i+1) * (i+2) < n:
    i = i + 1

if i * (i+1) * (i+2) == n:
    print("%d eh o produto %d*%d*%d" %(n,i,i+1,i+2))
else:
    print("%d nao eh triangular" %(n))
