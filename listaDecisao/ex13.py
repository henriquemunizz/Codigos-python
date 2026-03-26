# 13. Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler
# 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido.
# Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.


while True:
    dia = int(input("Informe o dia: "))

    if dia < 1 or dia > 31:
        print("Erro: dia inválido.")
        continue
        
    mes = int(input("Informe o mês: "))
    if mes <= 0 or mes > 12:
        print("Erro: mês inválido.")
        continue

    elif mes in [4, 6, 9, 11] and  dia > 30:
        print("Erro: este mês possui no máximo 30 dias.")
        continue

    elif mes == 2 and (dia < 1 or dia > 28):
        print("Erro: fevereiro possui no máximo 28 dias.")
        continue
        
    ano = int(input("Informe o ano: "))
    print(f"Data válida: {dia}/{mes}/{ano}")
    break