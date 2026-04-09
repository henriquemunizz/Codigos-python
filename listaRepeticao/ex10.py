#10. Escreva um algoritmo que recebe um inteiro positivo n e calcula n! = 1 · 2 · 3 . . . ·(n − 1)· n.
#Por exemplo, se n = 6, então 6! = 1 · 2 · 3 · 4 · 5 · 6 = 720.

num = int(input("Escreva um número inteiro:"))

contador = num

while contador > 2:
    num = (contador - 1) * num
    print(num)
    contador -= 1