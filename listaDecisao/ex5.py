#A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
#trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
#da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
#apenas nos dias úteis, escreva um algoritmo que recebe:

#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora
#Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do
#trabalhador.

diasMes = int(input("Dias úteis do mês: "))
horasT = int(input("Total de horas trabalhadas pelo trabalhador: "))
salarioH = float(input("Ganho por hora: "))

salarioHextra = 0
horasExtraMes = 0
horasPorDia = horasT / diasMes

if horasPorDia > 8:
    horasExtrasMes = (horasPorDia - 8) * diasMes
    salarioHextra = horasExtrasMes * 0.5 * salarioH

salarioNormal = horasT * salarioH
salarioTotal = salarioNormal + salarioHextra

print(f"Horas extras trabalhadas: {horasExtrasMes}")
print(f"Sálario hora extra: {salarioHextra}")
print(f"Sálario total: {salarioTotal}")