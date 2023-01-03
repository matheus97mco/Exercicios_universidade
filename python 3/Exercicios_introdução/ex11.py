print("Informe dois numeros inteiros e um número real e depois calcule:")

n1 = int(input('1º numero inteiro: '))
n2 = int(input('2º numero inteiro: '))
n3 = float(input('numero real: '))

calculo1 = ((2*n1)*(n2/2))
calculo2 = ((3*n1)+n3)
calculo3 = (n3**3)

print("\nO produto do dobro do primeiro com metade do segundo eh:",calculo1)
print("\nA soma do triplo do primeiro com o terceiro eh:",calculo2)
print(f'\nO terceiro elevado ao cubo eh: {calculo3:.2f}')

