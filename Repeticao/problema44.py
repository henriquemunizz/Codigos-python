nota1 = float(input("Nota: "))

while nota1 < 0 or nota1 > 10:
    print("Nota inválida")
    nota1 = float(input("Digite novamente: "))


nota2 = float(input("Nota: "))

while nota2 < 0 or nota2 > 10:
    print("Nota inválida")
    nota1 = float(input("Digite novamente: "))

media = (nota1 + nota2) / 2

print(f"A nota inserida foi {media}")

