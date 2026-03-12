contas = {}


def criar_conta():
    nome = input("Digite o nome do titular: ")

    if nome in contas:
        print("Conta já existe.")
    else:
        contas[nome] = 0
        print("Conta criada com sucesso.")


def depositar():
    nome = input("Digite o nome da conta: ")

    if nome in contas:
        valor = float(input("Digite o valor do depósito: "))
        contas[nome] += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")


def sacar():
    nome = input("Digite o nome da conta: ")

    if nome in contas:
        valor = float(input("Digite o valor do saque: "))

        if valor > contas[nome]:
            print("Saldo insuficiente.")
        else:
            contas[nome] -= valor
            print("Saque realizado com sucesso.")
    else:
        print("Conta não encontrada.")


def consultar_saldo():
    nome = input("Digite o nome da conta: ")

    if nome in contas:
        print(f"Saldo atual: R$ {contas[nome]}")
    else:
        print("Conta não encontrada.")


def menu():

    while True:

        print("\n=== SISTEMA BANCÁRIO ===")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()

        elif opcao == "2":
            depositar()

        elif opcao == "3":
            sacar()

        elif opcao == "4":
            consultar_saldo()

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


menu()
