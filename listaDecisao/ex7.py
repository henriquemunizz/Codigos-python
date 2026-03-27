# 7. A raiz quadrada é uma operação que apenas aceita números positivos. Escreva um algoritmo
#que lê um número qualquer e retorna a raiz quadrada desse número se possível. Use a função
#math.sqrt(<numero>) para calcular a raiz quadrada em Python. Note que, para usar essa função,
#você terá que importar o módulo math antes.

import math

while True:
    num = float(input("Digite um número para descobrir a raiz quadrada: "))

    if num >= 0:
        raiz = math.sqrt(num)
        print(f"\nA raiz quadrada de {num} é igual a: {raiz}")
        break
    else:
        print("\nImpossível extrair raiz de número negativo!\n")
        continue


