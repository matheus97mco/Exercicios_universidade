print("Programa recebe dois números inteiros e gera os números inteiros que estão nesse intervalo e a soma deles!\n")

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

soma = 0

while n1 < n2:
    intervalo = n1
    n1 += 1
    print(intervalo, end =' ')
    soma += intervalo
    
while n1 >= n2:
    intervalo = n2
    n2 += 1 
    print(intervalo, end =' ')
    soma += intervalo

print("\nA soma do intervalo é:",soma)



 
