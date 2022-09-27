'''
 Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
3. Construir um programa em python que leia um número inteiro e positivo informado pelo usuário.  O programa deve imprimir todos os números pares entre 0 e o numero informado pelo usuário.  Depois, o programa deve imprimir todos os número ímpares entre 0 e o numero informado pelo usuário.  Este exercício deve ser implementado utilizando o comando for.

'''
valores = [[], []]
numero  = int(input(f'Digite o numero: '))
for i in range(0, numero):
    valor = i+1
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')

