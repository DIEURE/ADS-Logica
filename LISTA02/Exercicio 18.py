"""
DESCRICAO:
18. Faça um algoritmo para ler um número que é um código de usuário.
Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234)
deve ser apresentada a mensagem ‘Usuário inválido! ’.
Caso o Código seja correto, deve ser lido outro valor que é a senha.
Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’.
Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.
AUTOR: DIEURE
DATA: 25/09/2022

"""
usuario = int(input("Digite o codigo do usuario "))
userPadrao = 1234
password = 9999


if usuario == userPadrao:
    senha = int(input("Digite sua senha: "))
    if senha == password:
        print("Acesso permitido")
    else:
        print("Senha invalida !")

else:

    print("Usuario invalido")