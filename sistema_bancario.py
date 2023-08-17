import textwrap, os

def menu():
    menu = """
    =========== MENU ===========
    |                          |
    |  [1]. Depositar          |
    |  [2]. Sacar              |
    |  [3]. Extrato            |
    |  [4]. Nova conta         |
    |  [5]. Listar contas      |
    |  [6]. Excluir conta      |
    |  [7]. Novo usuário       |
    |  [8]. Sair               |
    |                          |
    ============================
    >> """
    return input(textwrap.dedent(menu)) # (textwrap.dedent): remove os espaçamentos criados pela identação

def depositar(saldo, valor, extrato):
    os.system("cls")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n>> Depósito realizado com sucesso!")
    else:
        print("\n>> Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, quantidade_saques, limite_saques):
    os.system("cls")

    if quantidade_saques >= limite_saques:
        print("\n>> Operação falhou! Número máximo de saques diários execido.")
    elif valor > limite:
        print("\n>> Operação falhou! O valor do saque excede o limite.")
    elif valor > saldo:
        print("\n>> Operação falhou! Você não tem saldo suficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        quantidade_saques += 1
        print("\n>> Saque realizado com sucesso!")
    else:
        print("\n>> Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, quantidade_saques
    
def exibir_extrato(saldo, /, *, extrato):
    os.system("cls")

    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n=========================================")

def criar_conta(agencia, numero_conta, usuarios):
    os.system("cls")

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        os.system("cls")
        print("\n>> Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    os.system("cls")
    print("\n>> Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    os.system("cls")

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def deletar_conta(contas, agencia, numero_conta):
    contas_para_remover = [] # lista que irá armazenar a conta que quero deletar

    for conta in contas:
        if numero_conta == conta['numero_conta'] and agencia == conta['agencia']:
            contas_para_remover.append(conta) # caso a conta com o 'numero_conta' passado pelo user existir, ela sera adcionada a lista
    
    for conta in contas_para_remover:
        contas.remove(conta) # deletando a conta (tambem poderia ser utilizado o metodo clear())

    os.system("cls")
    if contas_para_remover:
        print("\n>> Conta excluída com sucesso!")
    else:
        print("\n>> Conta não encontrada, fluxo de exclusão de conta encerrado!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    os.system("cls")
    
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        os.system("cls")
        print("\n>> Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    os.system("cls")
    print("\n>> Usuário criado com sucesso!")       

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "1":
            os.system("cls")
            valor = float(input("\nInforme o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            os.system("cls")
            valor = float(input("\nInforme o valor que deseja sacar: "))

            saldo, extrato, quantidade_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                quantidade_saques=quantidade_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            # numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "6":
            os.system("cls")

            numero_conta = int(input("Informe o número da conta que você deseja deletar: "))

            deletar_conta(contas, AGENCIA, numero_conta)

        elif opcao == "7":
            criar_usuario(usuarios)

        elif opcao == "8":
            break

        else:
            os.system("cls")
            print("\n>> Operação inválida. Por favor, selecione novamente a opração desejada.")

os.system("cls")
main()