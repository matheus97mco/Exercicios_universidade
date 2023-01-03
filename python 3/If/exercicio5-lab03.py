print("Leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar a mensagem conforme a media\n")

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2

if media == 10:
    print("A media foi",media,"! Portanto 'Aprovado com Distinção'")
elif media >= 7:
    print("A media foi",media,"! Portanto 'Aprovado'")
else:
    print("A media foi",media,"! Portanto 'Reprovado'")

