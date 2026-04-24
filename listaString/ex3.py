#3. Escreva um programa que recebe duas Strings: frase e letra; a frase representa um
#conjunto de caracteres e letra um único caracter. Sua função deverá substituir toda
#ocorrência do caracter letra contido frase pelo caracter *. Por exemplo, se frase for
#"Jabuticaba" e a letra for "a"então seu método deverá retornar "J*butic*b*". Note
#que, seu programa deverá funcionar independente da letra ser maiúscula ou minúscula, ou
#seja, toda letra "a"e "A"deve ser substituída. Considere que não há caracteres acentuados
#nas palavras e não deve ser usado o método replace neste exercício.

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

resultado = ""

for c in frase:
    if c.lower() == letra.lower():
        resultado += "*"
    else:
        resultado += c

print(resultado)