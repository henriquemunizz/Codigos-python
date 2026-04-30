#2. Escreva uma função que dado um inteiro positivo n, verifica se n é primo ou não.


def primo(n):
    if n < 2:
        print("Não é primo")
        return
    
    divisores = 0
    for contador in range(1, n + 1):
        if n % contador == 0:
            divisores += 1

    if divisores == 2:
        print("Número primo")
    else:
        print("Não é primo")

numero = int(input("Digite um número inteiro positivo: "))
primo(numero)