#6. Um número a é dito permutação de um número b se os dígitos de a formam uma permutação dos dígitos de b. Exemplo: 5412434 é uma permutação de 4321445, mas não é uma
#permutação de 4312455. Obs.: Considere que o dígito 0 (zero) não aparece nos números.

#a) Faça uma função contadigitos que dados um inteiro n e um inteiro d, 0 ≤ d ≤ 9, devolve
#quantas vezes o dígito d aparece em n.

def contadigitos(a, b):

    a_str = str(a)
    b_str = str(b)

    contador = 0
    pos = 0

    while True:
        aparece = a_str.find(b_str, pos)

        if aparece == -1:
            break

        contador += 1
        pos = aparece + len(b_str)

    return contador

a = input("Digite um número inteiro: ")
b = input("Digite outro número inteiro de 0 a 9: ")
print(contadigitos(a, b))