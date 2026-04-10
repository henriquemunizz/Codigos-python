cpf = int(input("Digite os 9 primeiros dígitos do CPF: "))

quociente = cpf

multiplicador = 2
soma1 = 0

# cálculo do primeiro dígito
while quociente != 0:
    digito = quociente % 10
    quociente = quociente // 10
    soma1 += digito * multiplicador
    multiplicador += 1

resto1 = soma1 % 11

if resto1 < 2:
    d10 = 0
else:
    d10 = 11 - resto1

# cálculo do segundo dígito
quociente = cpf
multiplicador = 3
soma2 = 0

while quociente != 0:
    digito = quociente % 10
    quociente = quociente // 10
    soma2 += digito * multiplicador
    multiplicador += 1

soma2 += d10 * 2

resto2 = soma2 % 11

if resto2 < 2:
    d11 = 0
else:
    d11 = 11 - resto2

print("Dígitos verificadores:", d10, d11)