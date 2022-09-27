"""
DESCRICAO:
19. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'.

"""
numeroConta = float(input("Digite o numero  da conta:  "))
saldo       = float(input("Digite o saldo   da conta conta:  "))
debito      = float(input("Digite o debito  da conta:  "))
credito     = float(input("Digite o credito da conta:  "))

saldo_atual = saldo - debito + credito

if saldo_atual >=0:
   print("SALDO POSITIVO")
else:
   print("SALDO NEGATIVO !")
