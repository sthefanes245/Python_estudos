""" 
Atividade: Escreva um programa que receba um saldo inicial e pergunte ao usuário se ele deseja [1] Sacar, [2] Depositar ou [3] Ver Extrato.

Requisitos:

No saque, verifique se o saldo >= saque. Se sim, subtraia; se não, informe "Saldo insuficiente".

Use uma estrutura aninhada ou if ternário para exibir o status final da operação.
"""
saldo = 5200.25
op = -1
historico = []

while op != 0:
    op = int(input("Escolha um opção:\n[1] Sacar, [2] Depositar, [3] Ver Extrato, [4] Voltar ao início ou [0] Finalizar:\n"))

    if op == 1:
        saque = float(input("informe o valor que deseja sacar:\n"))
        if(saldo >= saque):
            saldo -= saque
            print("Aguarde a contagem das cédulas...")

            historico.append(f"Saque de R${saque:.2f}")
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")
  
    elif op == 2:
        deposito = float(input("Informe o valor que deseja depositar:\n"))
        saldo += deposito
        historico.append(f"Deposito de R${deposito:.2f}")
        print("Deposito realizado!")

    elif op == 3:
        print("\n========== EXTRATO ==========")
        print(historico)
        print(f"Saldo = R${saldo}")  
        print("==============================")



print("Serviço finalizado!")