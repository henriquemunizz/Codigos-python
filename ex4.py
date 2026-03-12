#Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
#dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

num = int(input("Digite um número inteiro:"))
seg = int(input("Digite outro número inteiro:"))

soma = num + seg
subtração = num - seg
multiplicacao = num * seg
divisãoInt = num // seg
restoDiv = num % seg

print("A soma é ",soma , ",A subtração é ",subtração , ",A multiplicação é ", multiplicacao , ",A divisão é ",divisãoInt ,",e o resto da divisão é ", restoDiv)