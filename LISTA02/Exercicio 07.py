"""
DESCRICAO LER TRES NUMEROS INTEIROS INFORMADOS PELO USUARIO E IMPRIMIR EM ORDEM DESCRESCENTE
AUTOR: DIEURE
DATA: 29/08/2022
"""
import math
n1 = int(input("DIGITE O PRIMEIRO NUMERO "))
n2 = int(input("DIGITE A SEGUNDO  NUMERO "))
n3 = int(input("DIGITE A TERCEIRO NUMERO "))

if(n1 > n2 and n1 > n3):
    if(n2 > n3):
        print("ORDEM DECRESCENTE", n1, "-", n2, "-", n3)
    else:
         print("ORDEM DECRESCENTE", n1, "-", n3, "-", n2)

if(n2>n1 and n2>n3):
    if(n1>n3):
        print("ORDEM DECRESCENTE", n2, "-", n1, "-", n3)
    else:
        print("ORDEM DECRESCENTE", n2, "-", n3, "-", n1)

if(n3>n1 and n3>n2):
    if(n1>n2):
        print("ORDEM DECRESCENTE", n3, "-", n1, "-", n2)
    else:
        print("ORDEM DECRESCENTE", n3, "-", n2, "-", n1)