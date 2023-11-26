from datetime import datetime

class Cliente:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def para_string(self):
        print(f"Cliente -> Nome:{self.nome}   CPF:{self.cpf}")

class Conta:
    def __init__(self, cliente, numero_conta, saldo_inicial):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.historico = []
        self.data_criacao = datetime.now()  # Adiciona a data de criação ao inicializar a conta
        self.salvar_conta()  # Chama a função salvar_conta imediatamente após a criação da conta

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_movimento(f"Depósito de R${valor}")
        self.salvar_conta()

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.registrar_movimento(f"Saque de R${valor}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.depositar(valor)
            self.registrar_movimento(f"Transferencia de R${valor} para Conta {destino.numero_conta}")
        else:
            print("Saldo insuficiente para a transferencia.")

    def registrar_movimento(self, descricao):
        movimento = {
            "descricao": descricao,
            "saldo_atual": self.saldo
        }
        self.historico.append(movimento)
        self.salvar_conta()

    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta} - Saldo: R${self.saldo}")
        for movimento in self.historico:
            print(f"{movimento['descricao']} - Saldo: R${movimento['saldo_atual']}")

    def salvar_conta(self):
        with open(f"extrato_conta_{self.numero_conta}.txt", "w") as f:
            f.write(f"Extrato da Conta {self.numero_conta} - Saldo: R${self.saldo}\n")
            f.write(f"Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}\n")
            f.write(f"Data de Criacao: {self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')}\n")
            for movimento in self.historico:
                f.write(f"{movimento['descricao']} - Saldo: R${movimento['saldo_atual']}\n")

    def ler_extrato(self):
        file_name = f"extrato_conta_{self.numero_conta}.txt"
        try:
            with open(file_name, "r") as f:
                print(f"\nConteudo do arquivo '{file_name}':\n")
                print(f.read())
        except FileNotFoundError:
            print(f"Arquivo '{file_name}' nao encontrado.")

class HistoricoConta:
    def __init__(self):
        self.historicos = []

    @staticmethod
    def salvar_contas(contas):
        for conta in contas:
            conta.salvar_conta()
