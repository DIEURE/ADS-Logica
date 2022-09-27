#Autor: Dieure de Oliveira
#Data: 02/09/2022
#Descricao:
#Escreva um programa que faça a conversão de graus Farenheit para Centígrados. A
# conversão se dá pela seguinte fórmula: - C *= 5/9(F-32)

#Dados

grausF = int(input("Informe a  temperatura: "))

grausCent = (grausF - 32) * (5 / 9)

print("Graus centigrado eh: ", round(grausCent,2))
