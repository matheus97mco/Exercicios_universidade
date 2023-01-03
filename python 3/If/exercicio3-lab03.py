print("Verifique se uma letra digitada é 'F' ou 'M'. Conforme a letra escrever: F - Feminino, M -Masculino, Sexo Inválido.\n")

letra = str(input('Informe a letra correspondente ao sexo: ')) 

if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo Invalido!')



