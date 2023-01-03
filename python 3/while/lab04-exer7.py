print("Programa calcula e escreve o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B.(Usuario informa os dados)")

pais_A = int(input('Informe a população do país A: '))
pais_B = int(input('Informe a população do país B: '))

taxa_A = float(input('Informe a taxa do país A: '))
taxa_B = float(input('Informe a taxa do país B: '))

anos = 0

while pais_A < pais_B:
    pais_A += pais_A * taxa_A
    pais_B += pais_B * taxa_B
    anos += 1
    
print ("\nLevará",anos,"anos para que a população do pais A ultrapasse ou iguale a população do pais B, mantida as taxas de crescimento!")



