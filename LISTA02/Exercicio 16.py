"""
DESCRICAO:
16. Em matemática, a Sucessão de Fibonacci (também Sequência de Fibonacci), é uma sequência
de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente
(número de Fibonacci) corresponde a soma dos dois anteriores.
A sequência recebeu o nome do matemático italiano Leonardo de Pisa, mais conhecido por
Fibonacci (contração do italiano filius Bonacci), que descreveu, no ano de 1202, o crescimento
de uma população de coelhos, a partir desta.
Os números de Fibonacci são, portanto, os números que compõem a seguinte sequência: 0, 1,
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, …
A fórmula abaixo, implementa o cálculo de Fibonacci para o n-ésimo termo da sequência (este
valor é informado pelo usuário).
Implemente um programa em python que realize o cálculo do n-ésimo termo da sequência de
Fibonacci, utilizando a fórmula abaixo.
AUTOR: DIEURE
DATA: 03/09/2022
"""
import math

n = int(input("Digite o valor para o n-esimo elemento"))

fn = int(1/math.sqrt(5)* (((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n))
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
print(fn)