menu = f"""
=========== MENU ===========
|                          |
|  [1]. Depositar          |
|  [2]. Sacar              |
|  [3]. Extrato            |
|  [4]. Sair               |
|                          |
============================
>> """

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInforme o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("\nInforme o valor que desjea sacar: "))

        if quantidade_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários execido.")
        elif valor > 500:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saques += 1
            print(">> Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "4":
        break
    else:
        print("Opração inválida. Por favor, selecione novamente a opração desejada.")