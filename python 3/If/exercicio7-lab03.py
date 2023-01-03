print("Faça um Programa que leia três números e mostre o maior e o menor deles.")

n1 = float(input('Informe o primeiro numero: ')) 
n2 = float(input('Informe o segundo numero: '))
n3 = float(input('Informe o terceiro numero: '))

if n1 > n2 and n1 > n3 and n2<n3:
    print("O maior eh:",n1," e o menor eh:",n2)
elif n1 > n2 and n1 > n3 and n3<n2:
    print("O maior eh:",n1," e o menor eh:",n3)
elif n2 > n1 and n2 > n3 and n1<n3:
    print("O maior eh:",n2," e o menor eh:",n1)
elif n2 > n1 and n2 > n3 and n3<n1:
    print("O maior eh:",n2," e o menor eh:",n3)
elif n3 > n1 and n3 > n2 and n1<n2:
    print("O maior eh:",n3," e o menor eh:",n1)    
else:
    print("O maior eh:",n3," e o menor eh:",n2)   
    
