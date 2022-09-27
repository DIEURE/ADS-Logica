'''
Autor: Dieure
Oliveira
Data: 26 / 0
9 / 2022
Descrição:
2.
A
Sucessão
de
Fibonacci
é
uma
sequência
de
números
inteiros, começando
normalmente
por
0
e
1, na
qual, cada
termo
subsequente(numero
de
Fibonacci) corresponde
a
soma
dos
dois
anteriores.

'''

# n = int(input("Digite um numero: "))
# fibo = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)