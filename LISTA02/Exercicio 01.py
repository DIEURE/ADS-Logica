"""
DESCRICAO LER DOIS NUMEROS INTEIROS INFORMADOS PELO USUARIO E ENTAO IMPRIMIR O MAIOR
AUTOR: DIEURE
DATA:29/08/2022
"""
import math
n1 = int(input("DIGITE O PRIMEIRO NUMERO "))
n2 = int(input("DIGITE A SEGUNDO  NUMERO "))

if(n1 > n2):
    print("PRIMEIRO NUMERO EH MAIOR")
    print("MAIOR NUMERO:  ", n1)
    print("MENOR NUMERO:  ", n2)
else:
    print("O SEGUNDO NUMERO EH MAIOR:  ", n2)
    print("MAIOR NUMERO:  ", n2)
    print("MENOR NUMERO:  ", n1)

