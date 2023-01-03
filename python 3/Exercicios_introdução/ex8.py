print("Quanto você ganha por hora e o número de horas trabalhadas no mês?\n")

ganha_hr = input("Ganha por hora:")
horas_trab = input("Horas no mes:")

salario = (int(ganha_hr) * int(horas_trab))

print(f'\nO salario no mes foi de R${salario:.2f}!')
