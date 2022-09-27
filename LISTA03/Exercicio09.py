'''
9. Implementar um script em python que imprima todos os números entre 1 e 50. 
Ao final, o programa também deve imprimir o somatório destes números.
Este exercício deve ser implementado utilizando o comando for.
'''

soma = 0
for i in range(0, 50):
    i = i + 1
    soma = soma + i
    print(i)
print("-" * 31)
print("soma dos numeros de 1 a 50->", soma)
print("fim")
