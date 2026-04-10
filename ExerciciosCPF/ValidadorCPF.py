
cpf = int(input("CPF: "))

d1 = (cpf // 10000000000) % 10
d2 = (cpf // 1000000000) % 10
d3 = (cpf // 100000000) % 10
d4 = (cpf // 10000000) % 10
d5 = (cpf // 1000000) % 10
d6 = (cpf // 100000) % 10
d7 = (cpf // 10000) % 10
d8 = (cpf // 1000) % 10
d9 = (cpf // 100) % 10
d10 = (cpf // 10) % 10
d11 = (cpf // 1) % 10


soma1 = d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2
resto1 = soma1 % 11

if resto1 < 2:
    d10V = 0
else:
    d10V = 11 - resto1

soma2 = d1 * 11 + d2 * 10 + d3 * 9 + d4 * 8 + d5 * 7 + d6 * 6 + d7 * 5 + d8 * 4 + d9 * 3 + d10 * 2
resto2 = soma2 % 11

if resto2 < 2:
    d11V = 0

else:
    d11V = 11 - resto2

if d10 != d10V or d11 != d11V:
    print("CPF inválido")

else:
    print("CPF válido")


#502836408
#56402275832

print(f"{d1}{d2}{d3}.{d4}{d5}{d6}.{d7}{d8}{d9}-{d10V}{d11V}")