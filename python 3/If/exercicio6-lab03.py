print("Faça um Programa que leia três números e mostre o maior deles:")

n1 = float(input('Informe o primeiro numero: ')) 
n2 = float(input('Informe o segundo numero: '))
n3 = float(input('Informe o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print("O maior numero eh:",n1)
elif n2 > n1 and n2 > n3:
    print("O maior numero eh:",n2)
else:
    print("O maior numero eh:",n3)
