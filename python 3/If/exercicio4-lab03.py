print("Verifique se uma letra digitada é vogal ou consoante.\n")

letra = str(input('Informe uma letra para saber se eh vogal ou consoante: '))

if (letra == 'a') or (letra =='e') or (letra == 'i') or (letra == 'o') or (letra == 'u') or (letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U') :
    print("É VOGAL!")
else:
    print("É CONSOANTE!")
