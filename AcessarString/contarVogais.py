frase_a = "Terça é feriado"
frase_b = "Segunda feira nao tem aula"

print(frase_a[0])
print(frase_b[0])

i = 0
vogais = ('a', 'e', 'i', 'o', 'u')
contadorVogais = 0

while i < len(frase_b):
    print(frase_b[i])
    if frase_b[i] in vogais:
        contadorVogais += 1
    i += 1

print(f"Quantidade de vogais {contadorVogais}")