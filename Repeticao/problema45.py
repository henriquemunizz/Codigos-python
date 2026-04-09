num = int(input("Digite um número positivo: "))


while num <= 0:
    print("Número invalido!")
    num = int(input("Digite um número positivo: "))

i = 1

while num <= i:
    num -= 1
    print(f"{num}")