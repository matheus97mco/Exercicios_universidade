print("Programa que peça os lados do triângulo. Se os valores formarem um triângulo. indicar, se o mesmo é: equilátero, isósceles ou escaleno.")

l1 = int(input('Informe a medida do lado 1 do triangulo: '))
l2 = int(input('Informe a medida do lado 2 do triangulo: '))
l3 = int(input('Informe a medida do lado 3 do triangulo: '))

if (l1+l2) < l3 or (l1+l3) < l2 or (l2+l3) < l1:
    print("NÃO É TRIANGULO!")
elif l1 == l2 == l3:
    print("Triangulo Equilatero, tres lados iguais!")
elif l1 == l2 or l1 == l3 or l3 == l2:
    print("Triangulo Isosceles, quaisquer dois lados iguais!")
else:
    print("Triangulo Escaleno, tres lados diferentes!")




