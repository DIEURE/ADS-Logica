'''
Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
6. Construir um programa que leia um número inteiro e positivo informado pelo usuário.
O programa deve verificar se o número informado pelo usuário é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
Este exercício deve ser implementado utilizando o comando while.
'''
numero = int(input("Digite o numero: "))
i = 2
primo = 0
while i < numero and primo == 0:

   if numero % i == 0:
      primo = 1
      print("O numero informado não é primo ")
   i = i+1
if primo == 0:
      print("O numero informado é primo ")

print("Fim do programa")

