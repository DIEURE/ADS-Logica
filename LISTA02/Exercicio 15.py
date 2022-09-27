"""
DESCRICAO:
15.Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 366 dias,
um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos
múltiplos de 100 que não são múltiplos de 400). Isto é feito com o objetivo de manter o
calendário anual ajustado com a translação da Terra e com os eventos sazonais relacionados às
estações do ano.
O último ano bissexto foi 2020 e o próximo será 2024.
Fazer um programa que peça ao usuário para digitar um valor inteiro correspondente a um ano
qualquer. O programa deve informar ao usuário se o ano é bissexto ou não. Informar qual foi o
ano bissexto anterior e o próximo

AUTOR: DIEURE
DATA: 03/09/2022
"""

ano = int(input("Digite  o ano: "))
if ano % 4 == 0 and ano % 100 !=0 or ano %400 ==0:
    print('Ano {} é BISSEXTO'.format(ano))

elif(ano-1) % 4== 0 and (ano-1) % 100!=0 or (ano- 1) % 400 ==0:
    print("O ano não é bissexto")
    print("O ano bissexto anterior vai ser " + str(ano-1))

elif(ano-2) % 4== 0 and (ano-2) % 100!=0 or (ano- 2) % 400 ==0:
    print("O ano não é bissexto")
    print("O ano bissexto anterior vai ser " + str(ano-2))

elif(ano-3) % 4== 0 and (ano-3) % 100!=0 or (ano- 3) % 400 ==0:
    print("O ano não é bissexto")
    print("O ano bissexto anterior vai ser " + str(ano-3))

elif(ano-4) % 4== 0 and (ano-4) % 100!=0 or (ano- 4) % 400 ==0:
    print("O ano não é bissexto")
    print("O ano bissexto anterior vai ser " + str(ano-4))

if(ano+1) % 4== 0 and (ano+1) % 100!=0 or (ano+ 1) % 400 ==0:
    print("O ano bissexto posterior vai ser " + str(ano+1))
elif(ano+2) % 4== 0 and (ano+2) % 100!=0 or (ano+ 2) % 400 ==0:
    print("O ano bissexto posterior vai ser " + str(ano+2))
elif(ano+3) % 4== 0 and (ano+3) % 100!=0 or (ano+ 3) % 400 ==0:
    print("O ano bissexto posterior vai ser " + str(ano+2))
elif(ano+4) % 4== 0 and (ano+4) % 100!=0 or (ano+ 4) % 400 ==0:
    print("O ano bissexto posterior vai ser " + str(ano+4))