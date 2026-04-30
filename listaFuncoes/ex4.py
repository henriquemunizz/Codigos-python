#4. Usando a função do exercício anterior, escreva um programa que imprime os 100 primeiros
#números primos começando do número 2.

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
        return n
    else:
        primo_boolean = False


i = 2

while i <= 100:
    resultado = primo(i)
    if resultado != None:
        print(resultado)
    i += 1