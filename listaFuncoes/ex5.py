#5. Usando a função que verifica se um número é perfeito ou não, escreva um algoritmo que
#mostra todos os números perfeitos no intervalo de 1 a 50000 (cinquenta mil).

def numero_perfeito(n):
    if n < 1:
        return None

    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i

    if soma_divisores == n:
        return n

contador = 1

while contador <= 50000:
    resultado = numero_perfeito(contador)
    if resultado != None:
        print(resultado)
    contador += 1
