"""
DESCRICAO LER DOIS NUMEROS INTEIROS INFORMADOS PELO USUARIO E IMPRIMIR EM ORDM DESCRESCENTE
AUTOR: DIEURE
DATA: 29/08/2022
"""
import math
n1 = int(input("DIGITE O PRIMEIRO NUMERO "))
n2 = int(input("DIGITE A SEGUNDO  NUMERO "))

if(n1>n2):
    print("NUMERO EM ORDEM DECRESCENTE", n1, "-", n2)
else:
    print("NUMERO EM ORDEM DECRESCENTE", n2, "-", n1)