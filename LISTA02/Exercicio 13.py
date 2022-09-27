"""
DESCRICAO:
Escreva um programa em python que leia três números inteiros. Devemos verificar se com
as medidas destes três números conseguimos formar um triângulo.
Os critérios de verificação são:
 a) Só existe um triângulo se qualquer lado for menor que a soma dos outros dois;
 Os critérios abaixo se aplicam apenas se existir o triângulo:
 b) Se os três lados forem iguais, o triângulo é equilátero;
 c) Se dois lados forem iguais o triângulo é isósceles.
 d) Se a soma do quadrado de dois lados for igual ao quadrado do terceiro lado,
 então o triângulo é retângulo.
O programa deve informar ao usuário se os valores digitados formam ou não um triângulo e
também deve informar o tipo do triângulo.
AUTOR: DIEURE
DATA: 03/09/2022
"""
import math
n1 = int(input("DIGITE O PRIMEIRO NUMERO "))
n2 = int(input("DIGITE A SEGUNDO  NUMERO "))
n3 = int(input("DIGITE A TERCEIRO NUMERO "))

c2= n2**2
c3= n3** 2
c1=c2+c3==c3

if(n1+n2)<n3 or (n1+n3)<n2 or (n2+n3)<n1 :
    print("OS TRES LADOS FORMAM UM TRIANGULO")
elif n1==n2 and n1==n3 and n2==n3:
    print("o triângulo é equilátero")
elif n1==n2 or n1==n3 or n2==n3:
    print("o triângulo é isósceles.")
elif c1:
    print("o triângulo  retangulo.")
else:
    print("Os 3 lados nao formam um triangulo")