#Problema 4.2: Dado um n´umero inteiro positivo n, escreva um
#algoritmo que imprime a tabuada de n at´e o valor 10.

n = int(input("Informe um número: \n"))

i = 0

while i < 10:
    i += 1
    print(f"{n} x {i} = {n * i}")
    
