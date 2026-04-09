#1. Dada uma sequência de números inteiros onde o último elemento é o 0, escreva um algoritmo
#que calcula a soma dos números pares da sequência.

num = int(input("Digite um número inteiro: "))

soma = 0

while num != 0:
    soma += num
    num = int(input("Digite um número inteiro: "))

print(soma)