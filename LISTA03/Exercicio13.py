'''
13. Implemente um script em python de modo que o usuário informe um número e o programa
imprima como resultado todos os divisores daquele número. Este exercício deve ser
implementado utilizando o comando for.
Autor: Dieure Oliveira
Data:27/09/22
'''

num = int(input("Digite um numero: "))

for i in range(1, num):
    if num % i == 0:
        print(i)
