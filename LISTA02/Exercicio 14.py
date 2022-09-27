"""
#Autor: Dieure de Oliveira
#Data: 22/09/2022
DESCRICAO:
14. O exercício em questão consiste em resolver o problema do troco em um estabelecimento
comercial. No Brasil, temos moedas de 1 real, 50 centavos, 25 centavos, 10 centavos, 5 centavos
e 1 centavo. O problema do troco consiste em pagar um troco com a menor quantidade possível
de moedas. Por exemplo, para um troco de R$ 2,78, a solução ótima seria: 2 moedas de 1 real,
1 moeda de 50 centavos, 1 moeda de 25 centavos e 3 moedas de 1 centavo (total de 7 moedas).
É possível elaborar um programa em python para resolver este problema? Em caso afirmativo,
escreva um script em python para a resolução da questão.
"""
valor       = 3.61
troco       = valor * 100

# Moeda de 01 real
moeda1 = troco // 100
restoMoeda1 = troco % 100

# Moeda de 50 centavos
moeda50 = restoMoeda1 // 50
restoMoeda50 = restoMoeda1 % 50

# Moeda de 25 centavos
moeda25 = restoMoeda50 // 25
restoMoeda25 = restoMoeda50 % 25

# Moeda de 10 centavos
moeda10 = restoMoeda25 // 10
restoMoeda10 = restoMoeda25 % 10

# Moeda de 5 centavos
moeda5 = restoMoeda10 // 5
restoMoeda5 = restoMoeda10 % 5

# Moeda de 1 centavo
moeda01 = restoMoeda5 // 1
restoMoeda01 = restoMoeda5 % 1

totalMoedas = (moeda1+moeda50+moeda25+moeda10+moeda5+moeda01)*1

# Exibe na tela
print("========INICIANDO O TROCO=======")
if moeda01 > 0:
    print("O Total de moeda(s) 1.00 é. ", moeda1)
if moeda50 > 0:
    print("O Total de moeda(s) 0.50 é. ", moeda50)
if moeda25 > 0:
    print("O Total de moeda(s) 0.25 é. ", moeda25)
if moeda10:
    print("O Total de moeda(s) 0.10 é. ", moeda10)
if moeda5 > 0:
    print("O Total de moeda(s) 0.05 é. ", moeda5)
if moeda01 > 0:
    print("O Total de moeda(s) 0.01 é. ", moeda01)
print("================================")
print(f"TOTAL DE MOEDAS...........:  {round(totalMoedas)}")
print("================================")
print("FIM.")