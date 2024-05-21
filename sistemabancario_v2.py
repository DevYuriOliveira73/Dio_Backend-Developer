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
    
     
def cadastrar_usuario(list_usuario, nome1, dt_nascimento1, cpf1, endereco1):


    for usuario in list_usuario:
        if usuario.get('cpf') == cpf1:
            print(f'O CPF [{cpf1}] já está cadastrado')
            return list_usuario

    new_usuario = dict(
                    nome = nome1, 
                    dt_nascimento = dt_nascimento1, 
                    cpf = cpf1, 
                    endereco = endereco1
    )

    list_usuario.append(new_usuario)
    print(f'Usuário {nome1} cadastrado com sucesso.')
    return list_usuario

    '''

    FALTA:
    - somente numero d cpf
    - colocar para esse formato[endereco  string ( logradoro, nro - bairro - cidade/sigla estado)]

    '''
def procurar_usuario(list_usuario, cpf1):
    for usuario in list_usuario:
        if usuario.get('cpf') == cpf1:
            return usuario
    print("CPF não encontrado no banco de dados")
    return None


def existencia_usuario(list_bancaria, usuario):
    existe = False
    for cpf in list_bancaria:
        if cpf == usuario[cpf]:
            existe = True
            break
    return existe
        

def cadastrar_conta_bancaria(list_bancaria, usuario):
    
    if existencia_usuario(list_bancaria, usuario):
        nome_conta = f'Conta_{len(list_bancaria[usuario[cpf]])+1}'
        
        new_conta = {
                    'agencia': '0001',
                    'numero_conta': len(list_bancaria[usuario[cpf]])+1
        }
        list_bancaria[usuario[cpf]][nome_conta] = new_conta
    else:
        nome_conta = f'Conta_{1}'
        
        new_conta = {
                    'agencia': '0001',
                    'numero_conta': 1
        }
        list_bancaria[usuario[cpf]][nome_conta] = new_conta
        
'''##################################################'''
menu_usuario = """

[1] Selecionar Usuario
[2] Adicionar Usuario

=> """

menu_conta = """

[1] Adicionar Conta

"""



menu_conta = """

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

lista_usuarios = []
lista_bancaria = []

usuario_selecionado = None

while usuario_selecionado == None:
    opcao = input(menu_usuario)

    if opcao == '1':
        cpf = int(input("Digite o CPF: "))
        usuario_selecionado = procurar_usuario(lista_usuarios, cpf)

    elif opcao == '2':
        print("INFORME")
        nome = input('Seu nome: ')
        dt_nascimento = input("Sua data de nascimento: ")
        cpf = int(input("Seu CPF: "))
        endereco = input("Seu endereço: ")
        cadastrar_usuario(lista_usuarios, nome, dt_nascimento, cpf, endereco) 




while True:

    opcao = input(menu_conta)

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






    """
    

--	CADASTRAR USUARIO(CLIENTE)
armazenar os usuarios em uma lista

usuario [atributos] (nome, dt d nascimento, cpf e endereço)

endereco  string ( logradoro, nro - bairro - cidade/sigla estado)

somente numero d cpf

nao pode 2 CPFs




--	CADASTRAR CONTA BANCARIA
conta corrente

armazenar numa lista

conta [atributos] (agencia, numero d conta, usuario)
numero da conta eh sequencial (1,2,3,4...)
agencia (0001) ever


--	listar contas




PARA VINCULAR UM USUARIO A UMA CONTA, FILTRE A LISTA DE USUARIOS BUSCANDO O NUMERO DO CPF INFORMADO PARA CADA USUARIO DA LISTA
    """