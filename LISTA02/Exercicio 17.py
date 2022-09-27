"""
DESCRICAO:
17. Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as
idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e
escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das
idades do homem mais novo com a mulher mais velha.

AUTOR: DIEURE
DATA: 12/09/2022

"""
h1 = int(input("Digite a idade do 1ª Homem "))
h2 = int(input("Digite a idade do 2ª Homem "))
m1 = int(input("Digite a idade da 1ª Mulher "))
m2 = int(input("Digite a idade da 2ª Mulher "))


somaH = h1 + h2
somaM = m1 + m2

if h1 > h2 and m1 < m2:

    somaHM = h1 + m1
    produto = h2 * m2
    print("Result",somaHM )
    print("Produto", produto)

elif h2 > h1 and m2 < m1:
    somaHVM = h2 + m2
    produto2 = h1 * m1
    print("A soma de idade do homem mais velho e da mulher mais nova ",somaHVM )
    print("O produto das idades do homem mais novo com a mulher mais velha ", produto2)