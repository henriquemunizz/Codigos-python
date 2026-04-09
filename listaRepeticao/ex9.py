#9. Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de
#tempo em meses t, escreva um algoritmo que calcula o valor final em dinheiro se d ficar
#aplicado a taxa de juros j durante t meses.

dinheiro = float(input("Dinheiro: "))
jurosPorcentagem = float(input("Juros por mês em %: "))
meses = int(input("Meses: "))

juros = jurosPorcentagem / 100
contador = 1

while contador <= meses:
    desconto = dinheiro * juros
    dinheiro -= desconto
    print(f"Mês: {1} Dinheiro: {dinheiro: .2f}")
    contador += 1