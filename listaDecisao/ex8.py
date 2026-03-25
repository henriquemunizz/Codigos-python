#8. Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
#tabela a seguir:
#Categoria Idade
#Infantil 5 a 7
#Juvenil 8 a 10
#Adolescente 11 a 15
#Adulto 16 a 30
#Senior acima de 30

nome = input("Nome do Nadador: ")
idade = int(input("Idade do Nadador: "))

if idade >= 5 and idade <=7 :
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print("Categoria: Infantil")
if idade >= 8 and idade <=10 :
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print("Categoria: Juvenil")
if idade >= 11 and idade <=15 :
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print("Categoria: Adolescente")
if idade >= 16 and idade <=30 :
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print("Categoria: Adulto")
if idade > 30:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print("Categoria: Sênior")

