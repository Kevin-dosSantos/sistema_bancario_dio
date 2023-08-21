
menu = """
[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair

"""

saldo = 1000
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE_DIARIO = 3

while True:
    print("======MENU======")
    print (f"Saldo atual:{saldo}")
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso! \n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_valor_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUE_DIARIO

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! Limite de saque diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!\n")

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
          print("\n========== EXTRATO ==========")
          print("Não foram realizadas movimentações." if not extrato else extrato)
          print(f"\nSaldo: R$ {saldo:.2f}")
          print("=============================\n")

    elif opcao == "0":
        break

    else:
        print("Operação inválida! Por favor, selecione uma das opções acima.\n")