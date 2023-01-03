print("Informe a altura(h) de uma pessoa e calcule o peso ideal para homens e mulheres!")

h = float(input('altura: '))

peso_h = ((72.7* h) - 58)
peso_m = ((62.1* h) - 44.7)

print(f'\nO peso ideal para homens eh: {peso_h:.2f} e para mulheres eh: {peso_m:.2f}')

