#3. Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
#positivos dele: o 1 e o próprio n. Escreva uma função que recebe um inteiro n e retorna o
#valor True se n é primo ou False se ele não for primo.

def primo(n):
    
    primo_boolean = True
   
    if n < 2:
        primo_boolean
        return
    
    divisores = 0
    for contador in range(1, n + 1):
        if n % contador == 0:
            divisores += 1

    if divisores == 2:
        primo_boolean
    else:
        primo_boolean = False

    return primo_boolean

numero = int(input("Digite um número inteiro positivo: "))
print(primo(numero))

