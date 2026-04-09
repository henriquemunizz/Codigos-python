#6. Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que
#cada questão vale 1 ponto, escreva um algoritmo que lê a pontuação da prova obtida de cada
#um dos candidatos e calcula:
#a) a maior e a menor nota
#b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram
#de 21 a 50 e o percentual que acertou acima de 50 questões

total_candidatos = 20
contador = 1

maior_nota = -1
menor_nota = 71

ate_20 = 0
de_21_50 = 0
acima_50 = 0

while contador <= total_candidatos:
    nota = int(input(f"Digite a nota do candidato {contador} (0 a 70): "))


    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

    if nota <= 20:
        ate_20 += 1
    elif nota <= 50:
        de_21_50 += 1
    else:
        acima_50 += 1

    contador += 1

perc_ate_20 = (ate_20 / total_candidatos) * 100
perc_21_50 = (de_21_50 / total_candidatos) * 100
perc_acima_50 = (acima_50 / total_candidatos) * 100

# Resultados
print("\nResultados:")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Até 20 questões: {perc_ate_20:.2f}%")
print(f"De 21 a 50 questões: {perc_21_50:.2f}%")
print(f"Acima de 50 questões: {perc_acima_50:.2f}%")