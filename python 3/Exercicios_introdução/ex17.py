print("Informe quanto você ganha por hora e o número de horas trabalhadas no mês e depois calcule os impostos referentes ao seu salário!\n") 

ganha_hr = int(input("Ganha por hora:"))
horas_trab = int(input("Horas no mes:"))

salario_bruto= (ganha_hr * horas_trab)
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = (salario_bruto - IR - INSS - sindicato)

print(f'\nO salario bruto no mes foi de R${salario_bruto:.2f}!')
print(f'\nA taxa de imposto de renda foi de R${IR:.2f}!')
print(f'\nA taxa de inss foi de R${INSS:.2f}!')
print(f'\nA taxa de sindicato foi de R${sindicato:.2f}!')
print(f'\nPortanto, o salario liquido no mes foi de R${salario_liquido:.2f}!')
