print("Programa que leia 5 números e informe a soma e a media.")

n = 0
aux = 1
soma = 0

while aux <= 5 : 
    numero = int(input("Informe um número: "))
    
    if numero > n:
        n = numero
    aux += 1
    soma += numero

media = soma/5

print("A soma dos 5 numeros é: ",soma)
print("A media dos 5 numeros é: ",media)


