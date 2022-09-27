'''
Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
5. Construir um programa que leia um número inteiro e positivo informado pelo usuário.
O programa deve verificar se o número informado pelo usuário é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
Este exercício deve ser implementado utilizando o comando for.
Autor: Dieure Oliveira
Data: 26/09/2022
'''
numero = int(input("Digite o numero: "))
mult =0
for i in range(2, numero):
   if numero % i == 0:
      mult = mult +1
if mult == 0:
   print("o numero informado é primo")
else:
   print("O numero informado não é primo")
print("Fim do programa")
