class SaldoInsuficienteError(Exception):
    def __init__(self, messagem='', saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = "Saldo Insuficiente para efetuar a transação  " \
              f"Saldo atual: {self.saldo}  Valor a ser sacado: {self.valor}"
        super(SaldoInsuficienteError, self).__init__(messagem or msg, *args)

