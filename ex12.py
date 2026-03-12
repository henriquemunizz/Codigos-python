#O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
#o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.
#Dica: realize várias divisões e restos de divisões por 10.

rm = int(input("Digite seu RM:"))

centmil = (rm // 100000) % 10
dezmil = (rm // 10000) % 10
mil = (rm // 1000) % 10
cent = (rm // 100) % 10
dezena = (rm // 10) % 10
unidade = (rm // 1) % 10


soma = + centmil + dezmil + mil + cent + dezena + unidade

print(soma)

