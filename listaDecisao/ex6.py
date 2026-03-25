#6. Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

numa = int(input("Digite um número (A): "))
numb = int(input("Digite outro número (B): "))

div = numa / numb

if numa % numb == 0:
    print(f"A é divisível por B ({div})")