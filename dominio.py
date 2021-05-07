from exececoes_negocio import SaldoInsuficienteError


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.__nome = nome
        self.__cpf = cpf
        self.__profissao = profissao

    def __repr__(self):
        return f'\nNome: {self.nome}\nCPF: {self.cpf}\nProfissao: {self.profissao}\n'    

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome      

    @property
    def cpf(self):
        return self.__cpf 

    @property
    def profissao(self):
        return self.__profissao  

    @profissao.setter
    def profissao(self, nova_profissao):
        self.__profissao = nova_profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None
    codigo_banco = "001"

    def __init__(self, cliente: Cliente, agencia, numero):
        self.__cliente = cliente
        self._set__numero(numero)
        self._set__agencia(agencia)
        self.__saldo = 0
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas   

    def __repr__(self):
        return f'\nCliente: {self.cliente}\nNumero da Conta: {self.numero}\
                 \nAgência: {self.agencia}\nCódigo Banco: {ContaCorrente.codigo_banco}\nSaldo: {self.saldo}\n'

    @property
    def cliente(self):
        return self.__cliente.nome 

    @property
    def numero(self):
        return self.__numero
    
    def _set__numero(self, numero):
        if not isinstance(numero, int):
            raise ValueError("O atributo número deve ser um inteiro.", numero)
        elif numero <= 0:
            raise ValueError("O atributo número deve ser maior que zero.", numero)
        self.__numero = numero    

    @property
    def agencia(self):
        return self.__agencia  

    def _set__agencia(self, agencia):
        if not isinstance(agencia, int):
            raise ValueError("O atributo agência deve ser um inteiro.", agencia)
        elif agencia <= 0:
            raise ValueError("O atributo agência deve ser maior que zero.", agencia)        
        self.__agencia = agencia

    @property
    def saldo(self):
        return self.__saldo      

    @staticmethod
    def retorna_total_contas_criadas():
        return ContaCorrente.total_contas_criadas

    def depositar(self, valor):    
         self.__saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O Valor a ser sacado não pode ser menor que zero")
        if self.__saldo < valor:
            raise SaldoInsuficienteError(saldo=self.saldo, valor=valor)
        self.__saldo = (self.__saldo - valor)

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O Valor a ser sacado não pode ser menor que zero")
        if self.__saldo < valor:
            raise SaldoInsuficienteError(saldo=self.saldo, valor=valor)
        self.sacar(valor)
        favorecido.depositar(valor)
