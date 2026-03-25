#2. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate.

numa = int(input("Digite um número: "))
numb = int(input("Digite outro número: "))

if numa > numb:
    print("O primeiro número é maior que o segundo")
elif numa < numb:
    print("O segundo número é maior que o primeiro")
else:
    print("Empate!")