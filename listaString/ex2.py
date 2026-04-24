#2. Crie um programa que imprime uma String contendo os caracteres da entrada palavra separados por espaços. Por exemplo, se a entradao for a palavra "Manga", seu programa deverá
#imprimir "M a n g a ".

palavra = input("Digite uma palavra: ")

for letra in palavra:
    print(letra, end=" ")