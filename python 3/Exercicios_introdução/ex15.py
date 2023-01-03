print("Informe o tamanho da area para calcular quantas latas de tinta precisam e o valor gasto!")
tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho/3

if tamanho % 54 == 0: #regra de 3: se 1 litro pinta 3 mts, 18 = x, x = 54
	latas = tamanho / 54
else: 
	latas = int(tamanho/54) + 1 #não tem como comprar meia lata de tinta, portanto +1

preco = latas * 80

print('\nPrecisa de',latas,'latas de tinta para pintar uma area de',tamanho,'metros!')
print(f'\nO preço total eh de: R${preco:.2f} reais!')
