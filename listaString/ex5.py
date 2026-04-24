#5. Dados duas strings (um contendo uma frase e outro contendo uma palavra), determine o
#número de vezes que a palavra ocorre na frase. Exemplo: Para a palavra ANA e a frase:
#ANA E MARIANA GOSTAM DE BANANA
#Temos que a palavra ocorre 4 vezes na frase. Escreva um programa que resolve o problema
#acima, seu programa deverá receber as duas strings e retornar o número de ocorrências da
#palavra na frase.
#Sugestão: use o método find da String.

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

contador = 0
pos = 0

while True:
    aparece = frase.find(palavra, pos)
    
    if aparece == -1:
        break
    
    contador += 1
    pos = aparece + len(palavra)

print(f"A quantidade que a palavra '{palavra}' aparece na frase é {contador}")