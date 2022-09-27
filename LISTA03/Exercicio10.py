'''
9. Implementar um script em python que imprima todos os números entre 1 e 50. 
Ao final, o programa também deve imprimir o somatório destes números.
Este exercício deve ser implementado utilizando o comando while.
'''

soma = 0
c=0
while c < 50:
    c = c + 1
    soma = soma + c
    print(c)
print("-" * 31)
print("soma dos numeros de 1 a 50->", soma)
print("fim")
