print("Programa que le três números e mostre-os em ordem decrescente!")

n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o segundo numero: '))
n3 = float(input('Informe o terceiro numero: '))

if n1 < n2  < n3:
    print("Os numeros em ordem decrescente sao:","|",n3,",",n2,",",n1,"|")
elif n1 < n3 < n2:
    print("Os numeros em ordem decrescente sao:","|",n2,",",n3,",",n1,"|")
elif n2 < n1 < n3:
    print("Os numeros em ordem decrescente sao:","|",n3,",",n1,",",n2,"|")
elif n2 < n3 < n1:
    print("Os numeros em ordem decrescente sao:","|",n1,",",n3,",",n2,"|") 
elif n3 < n1 < n2:
    print("Os numeros em ordem decrescente sao:","|",n2,",",n1,",",n3,"|")
elif n3 < n2 < n1:
    print("Os numeros em ordem decrescente sao:","|",n1,",",n2,",",n3,"|")
else:
    print("Existem numeros iguais, portanto não tem ORDEM DECRESCENTE!")
