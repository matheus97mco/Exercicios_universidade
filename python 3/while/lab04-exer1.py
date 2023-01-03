print("Programa que pede ao usuario 2 números e imprima a soma dos valores dentro do intervalo:")

num1 = int(input('Informe o 1º numero: '))
num2 = int(input('Informe o 2º numero: '))

total = 0

while num1 <= num2:
    total += num1
    num1 += 1

print("Soma dos valores dentro do intervalo: ",total)

