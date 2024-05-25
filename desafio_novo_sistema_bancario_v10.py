# Otimizando o Sistema Bancário com Funções Python

# Exibindo o menu
def menu():
    print("""\nInforme a opção desejada abaixo:

[1] Cadastrar novo usuário
[2] Abertura de conta
[3] Listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[0] Sair do sistema
""")

# Cadastrando clientes
def cadastrar_cliente(clientes, endereco):
    cpf = input("\nInforme o CPF (apenas números): ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print("\n>>> CPF já cadastrado anteriormente!\n")
        return
    
    nome = input("\nDigite o seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento no formato dd/mm/aaaa: ")
    logradouro = input("Informe Rua/Avenida: ")
    numero_casa = input("Informe o número da casa: ")
    tipo_casa = input("Tipo casa/apartamento? ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla do estado (exemplo: SP, MG...): ")
    endereco.append({"logradouro": logradouro, "numero_casa": numero_casa, "tipo_casa": tipo_casa, "bairro": bairro, "cidade": cidade, "estado": estado})
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n>>> Cliente cadastrado com sucesso!\n")


# Filtrando clientes
def filtrar_usuario(cpf, clientes):
    clientes_pesquisados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_pesquisados[0] if clientes_pesquisados else None


# Cadastrando uma conta
def cadastrar_conta(agencia, numero_conta, clientes):
    cpf = input("\nInforme o CPF do cliente (apenas números): ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print("\n>>> Contra cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n>>> Cliente não encontrado, por favor, inicie o cadastro.")


# Buscando contas
def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f""">>> Titular:\t{conta["cliente"]["nome"]}
>>> CPF:\t{conta["cliente"]["cpf"]}
>>> Agência:\t{conta["agencia"]}
>>> Conta:\t{conta["numero_conta"]}
""")
        print("=" * 40)

# Depositando
def depositar(valor, saldo, extrato, dep):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito {dep}: R$ {valor:.2f}\n"
        dep += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, dep

# Sacando
def sacar(saque, numero_saques, LIMITE_SAQUES, saldo, limite, extrato):

    if numero_saques < LIMITE_SAQUES and saldo >= limite:
        saldo -= saque
        numero_saques += 1
        extrato += f"Saque {numero_saques}/{LIMITE_SAQUES}: R$ {saque:.2f}\n"
        print("\nSaque realizado com sucesso!")

    elif numero_saques < LIMITE_SAQUES and saque > limite:
        print("\nSaque acima do valor limite!")

    elif numero_saques == LIMITE_SAQUES:
        print(f"\nVocê já fez {LIMITE_SAQUES} saques no período!")
        print("Por favor, aguarde o próximo período!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")
        print(f"Saldo insuficiente! \nSaldo: R$ {saldo:.2f}")

    return saldo, numero_saques, extrato

# Exibindo o Extrato
def exibir_extrato(extrato, saldo):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

    return extrato, saldo


# Função principal
def iniciar_sistema():
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500
    AGENCIA = "0001"
    extrato = ""
    numero_conta = 0
    limite = 0
    saldo = 0
    saques = 0
    numero_saques = 0
    dep = 1
    clientes = []
    cliente = []
    conta = 0
    contas = []
    endereco = []

    while True:
        menu()

        opcao = int(input("===> "))

        if opcao == 1:
            cadastrar_cliente(clientes, endereco)

        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == 3:
            listar_contas(contas)

        elif opcao == 4:
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato, dep = depositar(valor, saldo, extrato, dep)

        elif opcao == 5:
            saque = float(input("\nQual o valor do saque? "))
            saldo, numero_saques, extrato = sacar(saque, numero_saques, LIMITE_SAQUES, saldo, limite, extrato)

        elif opcao == 6:
            exibir_extrato(extrato, saldo)
            
        elif opcao == 0:
            print("\nOperação encerrada.")
            break

        else:
            print("""\nOperação inválida!
                    Por favor, selecione novamente a operação desejada.""")

print("\nSeja bem-vindo ao novo Sistema Bancário!")

iniciar_sistema()
