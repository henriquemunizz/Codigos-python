salario = float(input("Salário: "))
desconto = 0

ali1 = 1621 * 0.075
ali2 = (2902.84 - 1621) * 0.09
ali3 = (4354.37 - 2902.84) * 0.12

if salario <= 1621.00:
    desconto = salario * 0.075
elif salario <= 2902.84:
    desconto = ali1 + (salario - 1621) * 0.09
elif salario <= 4354.27:
    desconto = ali1 + ali2 + (salario - 2902.84) * 0.12
elif salario <= 8475.55:
    desconto = ali1 + ali2 + ali3 + (salario - 4354.27) * 0.14
else:
    desconto = 1182.92

print(f"Desconto INSS: {desconto}")
print(f"Salário Bruto {salario - desconto}")
