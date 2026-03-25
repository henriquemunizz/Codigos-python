# 7. A raiz quadrada é uma operação que apenas aceita números positivos. Escreva um algoritmo
#que lê um número qualquer e retorna a raiz quadrada desse número se possível. Use a função
#math.sqrt(<numero>) para calcular a raiz quadrada em Python. Note que, para usar essa função,
#você terá que importar o módulo math antes.

import math

num = int(input("Digite um número natural: "))

raiz = math.sqrt(num)

print(f"Raiz quadrada: {raiz}")

