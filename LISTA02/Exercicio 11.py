#Autor: Dieure de Oliveira
#Data: 02/09/2022
#Descricao:
#Construir um programa para calcular o IMC (Índice de Massa Corpórea) de uma pessoa,
#considerando a seguinte tabela:

#Dados

peso     = float(input("Informe o Peso: "))
altura   = float(input("Informe a Altura: "))

resultado = peso/(altura * altura)

if(resultado <19.1):
    print("Abaixo do peso")
elif(resultado >19.1 and resultado <=25.8):
    print("Peso Ideal")
elif(resultado >25.8 and resultado <27.3):
    print("Um pouco acima do peso")
elif(resultado >27.3 and resultado <=32.3):
    print("Muito acima do peso")
elif(resultado >32.3):
    print("Observacao: Obesidade")
else:
    print("\n")
print("Peso do paciente: ", peso)
print("Altura do paciente: ", altura)
print("IMC calculado: ", round(resultado,2))
