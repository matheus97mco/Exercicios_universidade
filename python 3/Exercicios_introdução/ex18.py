print("Informe o tamanho da area para calcular quantas latas de tinta precisam e o valor gasto!")

tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho/6

#lata de tinta
if tamanho % 108 == 0: #regra de 3: se 1 litro pinta 6 mts, 18 = x, x = 108
	latas = tamanho / 108
else: 
	latas = int(tamanho/108) + 1 #não tem como comprar meia lata de tinta, portanto +1

preco_lata = latas * 80

#galao de tinta
if tamanho % 21.6 ==0: #regra de 3: se 1 litro pinta  6 mts, 3,6 = x, x = 21,6
    galao = tamanho / 21.6
else:
    galao = int(tamanho/21.6) + 1 #não tem como comprar meio galao de tinta, portanto +1
    
preco_galao = galao * 25

#mistura
#preco_mistura = (preco_lata + preco_galao) * 0.1 

print('\nPrecisa de',latas,'latas ou',galao,'galoes de tinta para pintar uma area de',tamanho,'metros!')

print(f'\nO preço total APENAS PARA LATAS DE TINTA eh de: R${preco_lata:.2f} reais!')
print(f'O preço total APENAS PARA GALOES DE TINTA eh de: R${preco_galao:.2f} reais!')

#print(f'O preço total misturando lata e galoes eh de: R${preco_mistura:.2f} reais!')
#não consegui fazer a mistura!