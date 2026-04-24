#4. Escreva um programa que recebe duas Strings: frase e letras; a frase representa um
#conjunto de caracteres e letras alguns caracteres. Seu programa deverá substituir cada
#caracter c contido na frase pelo caracter * se este caracter c estiver presente em letras.
#Por exemplo, se a frase for:
#I can only show you the door.
#You’re the one that has to walk through it.
#e letras for aro então seu método deverá retornar:
#I c*n *nly sh*w y*u the d***.
#Y*u’re the one th*t h*s t* w*lk th**ugh it
#Note que, seu programa deverá funcionar independente da letra ser maiúscula ou minúscula,
#ou seja, toda letra "a"e "A" deve ser substituída e considere que não há caracteres acentuados
#nas palavras.

frase = input("Digite uma frase: ")
letras = input("Digite uma ou mains letras: ")

resultado = ""

for c in frase:
    if c.lower() in letras.lower():
        resultado += "*"
    else:
        resultado += c

print(resultado)