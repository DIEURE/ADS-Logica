"""
DESCRICAO Verificar se um dado número inteiro é par ou ímpar, positivo ou negativo.
AUTOR: DIEURE
DATA: 29/08/2022
"""

num1 = int(input("DIGITE UM NUMERO "))

if(num1%2)== 0:
    print("O NUMERO DIGITADO EH PAR")
else:
    print("O NUMERO DIGITADO EH IMPAR")
if(num1 >= 0):
    print("O NUMERO EH POSITIVO")
else:
    print("O NUMERO EH NEGATIVO")