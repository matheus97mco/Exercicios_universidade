print("Programa que pergunte em que turno você estuda: M-Matutino ou V-Vespertino ou N-Noturno!")

turno = str(input("Em que turno você estuda? ")) 

if turno == 'M-Matutino':
    print("Bom Dia!")
elif turno == 'V-Vespertino':
    print("Boa Tarde!")
elif turno == 'N-Noturno':
    print("Boa Noite!")
else:
    print("Valor Inválido!")

