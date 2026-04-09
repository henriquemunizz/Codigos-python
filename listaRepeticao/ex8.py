#8. Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
#positivos dele: o 1 e o próprio n. Escreva um algoritmo que recebe um inteiro n e verifica
#se n é primo ou não.

n = int(input("Digite um número inteiro positivo: "))

contador = 1
divisores = 0

while contador <= n:
    if n % contador == 0:
        divisores += 1
    contador += 1

if divisores == 2:
    print("Número primo")
else:
    print("Não é primo")