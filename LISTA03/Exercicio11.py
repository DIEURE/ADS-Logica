'''
11. Implemente um script em python que imprima todos os números múltiplos de 2 ou 3 em um
intervalo definido pelo usuário. Este exercício deve ser implementado utilizando o comando for.
Autor: Dieure Oliveira
Data:27/09/22
'''

for i in range(0, 20):
    if i % 2 == 0:
        i = i + 2
        print(i)

'''
12. Implemente um script em python que imprima todos os números múltiplos de 2 ou 3 em um
intervalo definido pelo usuário. Este exercício deve ser implementado utilizando o comando
while.
Autor: Dieure Oliveira
Data:27/09/22
'''
x=0
while x <= 20:
    if(x%2==0):
        x = x+2
        print(x)