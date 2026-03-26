#14. Agora, vamos acrescentar na verificação de data os casos de ano bissexto, ou seja, o ano que
#fevereiro tem 29 dias. Um ano é bissexto se:
#a) o ano for divisível por 4
#b) anos múltiplos de 100, não são bissextos
#c) quando o ano for divisível por 400 ele é bissexto
#d) as últimas regras prevalecem sobre as primeiras
#Para exemplificar um pouco essas regras, observe que 1900 não foi bissexto mas 2000 foi.

while True:
    dia = int(input("Informe o dia: "))

    if dia < 1 or dia > 31:
        print("Erro: dia inválido.")
        continue
        
    mes = int(input("Informe o mês: "))
    if mes <= 0 or mes > 12:
        print("Erro: mês inválido.")
        continue

    elif mes in [4, 6, 9, 11] and dia > 30:
        print("Erro: este mês possui no máximo 30 dias.")
        continue
        J
    ano = int(input("Informe o ano: "))
    if mes == 2:
        if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)) and dia > 29:
            print("Erro: fevereiro em ano bissexto possui no máximo 29 dias.")
            continue
        elif dia > 28:
            print("Erro: fevereiro possui no máximo 28 dias.")
            continue
    
    print(f"Data válida: {dia}/{mes}/{ano}")
    break