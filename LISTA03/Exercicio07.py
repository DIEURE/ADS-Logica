'''
Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
7. Implementar um script em python que imprima os números pares entre 100 e 150.
Este exercício deve ser implementado utilizando o comando for.
'''
ini = 100
fim = 150
for i in range(ini, fim):
    valor = i+1
    if valor % 2 == 0:
        print(valor)


