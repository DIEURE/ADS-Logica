"""
DESCRICAO Que um usuário informe o raio de um círculo e então o programa imprima sua área.
AUTOR: DIEURE
DATA: 29/08/2022
"""
import  math

raio = float(input("DIGITE O RAIO DE UM CIRCULO "))

area = math.pi * math.pow(raio,2)

print("AREA DE UM CIRCULO")
print("VALOR DO RAIO = ", raio)
print("AREA TOTAL = ", round(area,2))
