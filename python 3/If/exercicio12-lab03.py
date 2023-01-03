print("Programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média, conceito e aprovação:")

n1 = float(input('Informe a nota1: '))
n2 = float(input('Informe a nota2: '))

media = (n1+n2)/2

if 9.0 <= media <= 10.0:
    print("As notas foram",n1,"e",n2,"! A media eh:",media,"! Esta entre 9.0 e 10.0, ou seja, conceito 'A', portanto 'APROVADO'!")
elif 7.5 <= media <= 9.0:
    print("As notas foram",n1,"e",n2,"! A media eh:",media,"! Esta entre 7.5 e 9.0 , ou seja, conceito 'B', portanto 'APROVADO'!")
elif 6.0 <= media <= 7.5:
    print("As notas foram",n1,"e",n2,"! A media eh:",media,"! Esta entre 6.0 e 7.5, ou seja, conceito 'C', portanto 'APROVADO'!")
elif 4.0 <= media <= 6.0:
    print("As notas foram",n1,"e",n2,"! A media eh:",media,"! Esta entre 4.0 e 6.0, ou seja, conceito 'D', portanto 'REPROVADO'!")
elif 0.0 <= media <= 4.0:
    print("As notas foram",n1,"e",n2,"! A media eh:",media,"! Esta entre 0.0 e 4.0, ou seja, conceito 'E', portanto 'REPROVADO'!")    
else:
    print("ERRO ao idenficar as notas e conceitos! Notas",n1,"e",n2,"não estão na media:",media,", ou seja, não há conceitos!")
    

