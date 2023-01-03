print("Programa que leia 5 números e informe o maior.")

n = 0
aux = 1

while aux <= 5 : 
    numero = int(input("Informe um número: "))
    if numero > n:
        n = numero
    aux += 1

print("O maior numero é:",n)
