from time import sleep

def autorizacao_deposito(valor):
    return valor > 0

def deposito(saldo, valor, extrato,/):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato


def autorizacao_saque(saldo, valor, limite, numero_saques, lim_saques):
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= lim_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False

        elif valor < 0:
            print("Operação falhou! Valor inválido.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False

        else: return True


def saque(*,saldo, valor, extrato):
            
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    return saldo, extrato
    
def f_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
     


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if autorizacao_deposito(valor):
            saldo, extrato = deposito(saldo,valor, extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")
            sleep(.75)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if autorizacao_saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES):
            numero_saques += 1
            saldo, extrato = saque(saldo =saldo,valor= valor,extrato= extrato)
        else:
            print("Tente novamente!")
            sleep(.75)


    elif opcao == "3":
        f_extrato(saldo, extrato)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        