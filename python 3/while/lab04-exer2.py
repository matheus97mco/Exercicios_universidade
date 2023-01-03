print("Escreva um programa que leia 10 notas e informe a média dos alunos.")

cont = 1
total = 0
nota = 0

while cont < 11:
    nota = float(input("Digite a "+str(cont)+'º nota do aluno: '))
    cont += 1
    total += nota

media = total/10

print("A media do aluno é: ",media)
