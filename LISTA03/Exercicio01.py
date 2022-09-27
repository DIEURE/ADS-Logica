'''
Autor: Dieure Oliveira
Data: 26/09/2022
Descrição:
1. O que é o fatorial de um número n? Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
Isso posto, escreva um programa em python que solicite ao usuário informar um número inteiro.O programa deve calcular o valor do fatorial e imprimir o resultado para o usuário. 1. O que é o fatorial de um número n? Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120 Isso posto, escreva um programa em python que solicite ao usuário informar um número inteiro.
O programa deve calcular o valor do fatorial e imprimir o resultado para o usuário.
Autor: Dieure Oliveira
Data: 26/09/2022
'''
# .solicite ao usuário informar um número inteiro

numero = int(input("Digite um numero: "))
mostrar = numero
fatorial = 1

while (numero > 0):
    fatorial = fatorial * numero
    numero = numero - 1

print("O Numero Fatorial de", mostrar, "é", fatorial)
