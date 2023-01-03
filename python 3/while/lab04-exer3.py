print("Programa recebe 2 numeros e como saida mostra os valores impares dentro desse intervalo!\n")

n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))

while n1 <= n2:
    if n1 % 2 != 0:
        print(n1)
    n1 = n1 + 1


