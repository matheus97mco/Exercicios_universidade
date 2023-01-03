print("Informe o peso de peixes e calcule o valor da multa em caso de excesso!")

peso = float(input("Infome o peso dos peixes: "))

if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print('O excesso de peso foi de',excesso,'kg, portanto, a multa é de R$',multa,"!")

else:
	print("SEM EXCESSO DE PESO, PORTANTO NAO PRECISA PAGAR MULTA!")
   