#Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor
#de π.

raio = float(input("Digite o raio do círculo:"))

pi =  3.141592

area = pi * (raio **2)
peri = 2 * pi * raio

print("àrea: ",area,"perímetro: ",peri)