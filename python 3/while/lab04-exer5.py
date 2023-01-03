print("Programa le nome de usuário e a senha e não aceita senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações\n")

nome = str(input('Nome do usuario: '))
senha = str(input('Digite a senha: '))

while nome == senha:
    print("ERRO! USUARIO E SENHA IGUAIS! POR FAVOR DIGITE NOVAMENTE AS INFORMAÇÕES!\n")
    nome = str(input('Nome do usuario: '))
    senha = str(input('Digite a senha: '))

print("Sucesso!")
