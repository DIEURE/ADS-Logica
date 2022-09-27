'''
Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
4. Construir um programa em python que leia um número inteiro e positivo informado pelo usuário. O programa deve imprimir todos os números pares entre 0 e o numero informado pelo usuário. Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero informado pelo usuário. Este exercício deve ser implementado utilizando o comando while.
'''

valores = [[], []]
fim = int(input("Digite o numero: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        valores[0].append(x)
        x = x + 1

    if x % 2 == 1:
        valores[1].append(x)
        x = x + 1

print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
