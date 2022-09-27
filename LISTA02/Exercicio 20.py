"""
DESCRICAO:
20. Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque
 e quantidade mínima em estoque de um produto.
 Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
 Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra',
 senão escrever a mensagem 'Efetuar compra'.
AUTOR: DIEURE
DATA: 25/09/2022

"""
qtdeAtual   = int(input("Digite a QTDE atual em ESTOQUE: "))
qtdeMax  = int(input("Digite a QTDE MAXIMA          : "))
qtdeMin  = int(input("Digite a QTDE MINIMA          : "))


qtdeMedia = (qtdeMax + qtdeMin)/2

if qtdeAtual >= qtdeMedia:
   print("NAO EFETUAR A COMPRA.")
else:
   print("EFETUAR A COMPRA !")
