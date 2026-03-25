#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
#um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
#deverá ler o número de camisas, o número de calças e o número de pares de sapato.

camisas = int(input("camisas:"))
calças = int(input("calças"))
sapatos = int(input("pares de sapato:"))

maneiras = calças * calças * sapatos

print("kits diferentes: ",maneiras)