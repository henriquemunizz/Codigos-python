#Transforme os seguintes n´umeros de bin´ario para decimal:
#101011, 10110 e 10001

num = int(input("Digite um número decimal: "))

quociente = num
multiplicador = 1
soma = 0

while quociente != 0:
    digito = quociente % 10
    quociente = quociente // 10
    multiplicado = multiplicador * digito
    soma = soma + multiplicado
    multiplicador = multiplicador * 2
    print(digito)
    print(soma)