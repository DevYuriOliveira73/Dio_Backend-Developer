menu = """Escolha a operação: 
    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Sair
    ... """

op1 = "Insira o valor do deposito: "
op2 = "Insira o valor do saque: "

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITE_DIARIO = 3


flag = True
while flag:
    opcao = int(input(menu))

    if opcao == 1:

        valor = int(input(op1))
        if(valor <= 0 or type(valor) != type(1)):
            print('Valor inválido')
        else:
            saldo += valor
            extrato += f'Deposito de R$ {valor}\t\t +\n'
        continue

    elif opcao == 2:

        valor = int(input(op2))
        if(numeroSaques >= LIMITE_DIARIO):
            print('Limite de saque atingido')
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Valor ultrapassa limite de saque")
        else:
            saldo -= valor
            numeroSaques +=1
            extrato += f'Saque de R$ {valor}\t\t -\n'

    elif opcao == 3:
        print("EXTRATO".center(20, '#'))
        print(extrato)

    elif opcao == 4:
        flag = False

    else:
        continue
