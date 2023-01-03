print("Programa imprime na tela os numeros impares entre 1 e 50!\n")

n1 = 1
n2 = 50

while n1 <= n2:
    if n1 % 2 != 0:
        print(n1, end = ' ')
    n1 += 1
