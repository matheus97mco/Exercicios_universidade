print("Programa pede uma nota entre 0 e 10! Caso o valor seja invalido, imprima uma mensagem de erro e peça um novo valor valido\n")

nota = float(input('Informe uma nota entre 0 e 10: '))

while (nota < 0) or (nota > 10):
    nota = float(input("Valor invalido! Digite novamente uma nota entre 0 e 10:\n"))
    
print("NOTA VALIDA, FIM!")
