#5. Escreva um algoritmo que, dados um número inteiro positivo n, imprime na tela a contagem
#de todos os divisores positivos de n.

num = int(input("Digite número positivo: "))

i = 1

while i <= num:
    if num % i == 0:
     print(f"{i}")
    i += 1
