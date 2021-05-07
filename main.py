from dominio import ContaCorrente, Cliente
import sys

lista_contas = []
condicao = True

def main():

    rodar_sistema = True

    while rodar_sistema:

        print("\n---SISTEMA DE GESTÃO DE CONTAS BYTEBANK---\n\n")
        print("1 - Criar Nova Conta         2 - Excluir Conta \n3 - Exibir contas criadas    4 - Sair\n")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
           cadastrar_conta()

        if opcao == 2:
            cancelar_conta()

        if opcao == 3:
            exibir_contas_cadastradas()

        if opcao == 4:
            rodar_sistema = False
            sys.exit() 


def cancelar_conta():
    print("\n---------CANCELAMENTO DE CONTA BYTEBANK----------\n\n")
    condicao = True
    while condicao:
        try:
            cancela_conta = input("\nDigite o numero da conta para cancelamento: ")
            index = 0
            for conta in lista_contas:
                if str(conta.numero) == cancela_conta:
                    lista_contas.pop(index)
                    print("Conta excluida com sucesso!")
                else:
                    print("Conta não encontrada")
                index += 1 
        except ValueError as E:
            print(E.args)
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()

        status = int(input("\nDeseja cancelar outra conta?\n1-Yes    2-No\n\nopção: "))
        if status == 1:
            condicao = True
        if status == 2:
            condicao = False


def exibir_contas_cadastradas():
    print("\n---------EXIBINDO CONTAS CADASTRADAS NO BYTEBANK----------\n\n")        
    for conta in lista_contas:
        print(conta)


def cadastrar_conta():
    print("\n---------CADASTRO DE CONTA BYTEBANK----------\n\n")
    condicao = True
    while condicao:
        try:
            nome    = input("\nEntre com o nome do cliente: ")
            agencia = int(input("Entre com a agencia do cliente: "))
            numero  = int(input("Entre com o numero da conta: "))
            cliente = Cliente(nome, "114.234.512-12", "Engenheiro de Software")
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            print("\nConta criada com sucesso\n\n")
            lista_contas.append(conta_corrente)
        except ValueError as E:
            print(E.args)
            sys.exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(lista_contas)} (s) contas criadas')
            sys.exit()

        status = int(input("Deseja adicionar uma nova conta?\n1-Yes    2-No\n\nopção: "))
        if status == 1:
            condicao = True
        if status == 2:
            condicao = False


if __name__ == "__main__":
    main()