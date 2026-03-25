#11. Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
#seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#código condição de pagamento
#1 A vista em dinheiro ou cheque, recebe 10% de desconto
#2 A vista no cartão de crédito, recebe 5% de desconto
#3 Em duas vezes, preço normal de etiqueta sem juros
#4 Em quatro vezes, preço normal de etiqueta mais juros de 7%

preco = float(input("Preço do produto: "))
condicao = int(input("Condição de pagamento (1,2,3,4): "))

desconto = 0

if condicao == 1:
    desconto = preco * 0.1
    print(f"Preço final: {preco - desconto}")
if condicao == 2:
    desconto = preco * 0.05
    print(f"Preço final: {preco - desconto}")
if condicao == 3:
    desconto = preco
    print(f"Preço final: {preco}")
if condicao == 4:
    desconto = preco * 0.07
    print(f"Preço final: {preco + desconto}")

