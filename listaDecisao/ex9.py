#9. No exercício da calculadora, visto em sala de aula, temos um problema com a operação
#de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma
#divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer
#tal operação.

valor = input (" Digite numero : ")
numA = float ( valor )
op = input (" Operador (+ -*/) : ")
valor = input (" Digite numero : ")
numB = float ( valor )

resultado = 0

if op == "+":
    resultado = numA + numB

if op == "-":
    resultado = numA - numB

if op == "*":
    resultado = numA * numB

if op == "/" and numB == 0:
    print("Não é possível dividir por 0!")

if op == "/":
    resultado = numA / numB

print (f" Resposta { resultado }")