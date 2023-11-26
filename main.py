###########################################
##Programa que simula um sistema bancario##
###########################################

from cliente import Conta, Cliente, HistoricoConta
import os
import time


def interface():
    print('''
    1-)Criar conta
    2-)Abrir conta
    ''')

def interface2():
    print('''
    1-)Depositar
    2-)Sacar
    3-)Transferir
    4-)Ler extrato
    ''')

def criarConta():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    cliente = Cliente(cpf, nome)

    numero_conta = input("Digite o numero da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))

    nova_conta = Conta(cliente, numero_conta, saldo_inicial)
    contas.append(nova_conta)

    nova_conta.salvar_conta()

    print(f"Conta {nova_conta.numero_conta} criada com sucesso.")
    return nova_conta

def animacao():
    os.system("cls")
    for i in range(1, 11):  
        print("Loading [" + "=" * i + " " * (10 - i) + "] " + str(i * 10) + "%")
        time.sleep(0.3)
        os.system('cls')

contas = []
historico_conta = HistoricoConta()
parar = False

while not parar:
    interface()
    resposta = int(input("Escolha uma opcao: "))
    
    if resposta == 1:
        nova_conta = criarConta()
        contas.append(nova_conta)
    elif resposta == 2:
        numeroConta = input("Digite o numero da conta que deseja acessar: ")
        contaAtual = None
        for conta in contas:
            if conta.numero_conta == numeroConta:
                contaAtual = conta
                break

        if contaAtual:
            interface2()
            opcao = int(input("Digite uma opcao: "))
            if opcao == 1:
                valor_deposito = float(input("Digite o valor do deposito: "))
                contaAtual.depositar(valor_deposito)
                animacao()
            elif opcao == 2:
                valor_saque = float(input("Digite o valor do saque: "))
                contaAtual.sacar(valor_saque)
                animacao()
            elif opcao == 3:
                destino_conta = input("Digite o numero da conta de destino: ")
                valor_transferencia = float(input("Digite o valor da transferencia: "))
                destino = next((c for c in contas if c.numero_conta == destino_conta), None)
                if destino:
                    contaAtual.transferir(destino, valor_transferencia)
                    animacao()
                else:
                    print("Conta de destino nao encontrada.")
            elif opcao == 4:
                contaAtual.ler_extrato() 
                animacao()
