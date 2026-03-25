#4. Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
#partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
#palavra EMPATE.

timea = int(input("Gols do Corinthians: "))
timeb = int(input("Gols do Palmeiras: "))

if timea > timeb:
    print("Corinthians Ganhou!")
elif timea < timeb:
    print("Palmeiras Ganhou!")
else:
    print("Empate!")