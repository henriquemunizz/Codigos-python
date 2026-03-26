#11. Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
#seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#código condição de pagamento
#1 A vista em dinheiro ou cheque, recebe 10% de desconto
#2 A vista no cartão de crédito, recebe 5% de desconto
#3 Em duas vezes, preço normal de etiqueta sem juros
#4 Em quatro vezes, preço normal de etiqueta mais juros de 7%

while True:
    preco = float(input("Preço do produto: "))
    print("1 A vista em dinheiro ou cheque, recebe 10% de desconto")
    print("2 A vista no cartão de crédito, recebe 5% de desconto")
    print("3 Em duas vezes, preço normal de etiqueta sem juros")
    print("4 Em quatro vezes, preço normal de etiqueta mais juros de 7%")
    condicao = int(input("Selecione uma das opções acima: "))

    desconto = 0

    if condicao < 1 or condicao > 4:
            print("\n Forma de pagamento inválida! Tente Novamente\n")
            continue
    else:
    
        match condicao:
            case 1:
                desconto = preco * 0.1
                print(f"\nO desconto foi de {desconto}, Você pagará: {preco - desconto}")
                break
            case 2:
                desconto = preco * 0.05
                print(f"\nO desconto foi de {desconto}, Você pagará: {preco - desconto}")
                break
            case 3:
                parcela = preco / 2
                print(f"\nVocê pagará: 2 x {parcela}")
                break
            case 4:
                desconto = preco * 0.07
                parcela = (preco + desconto) / 4
                print(f"\nVocê pagará: 4 x {parcela}")
                break

        