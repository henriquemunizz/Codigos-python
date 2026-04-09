#4. Dados n um inteiro positivo e uma sequência de n números reais, escreva um algoritmo que
#conta e imprime a quantidade de números positivos e a quantidade de números negativos.

n = int(input("Digite a quantidade de números: "))

contador = 1
positivos = 0
negativos = 0

while contador <= n:
    num = float(input(f"Digite o {contador}º número: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    contador += 1

print("\nResultados:")
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")