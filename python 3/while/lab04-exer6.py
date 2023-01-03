print("Programa calcula e escreve o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B.")

pais_A = 80000 
pais_B = 200000

taxa_A = 0.03
taxa_B = 0.015

anos = 0

while pais_A < pais_B:
    pais_A += pais_A * taxa_A
    pais_B += pais_B * taxa_B
    anos += 1
    
print ("\nO numero de anos necessários para que a população do pais A ultrapasse ou iguale a população do pais B, mantida as taxas de crescimento será de:",anos, "anos!")
