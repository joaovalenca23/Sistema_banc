
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor que deseja depositar: '))

        if valor > 0:
            saldo +=  valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! Valor informado é inválido')
    elif opcao == '2':
        valor = float(input('Informe o valor do saque:'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operaçaõ falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operaçaõ falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operaçaõ falhou! Número máximo de saques diário excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido')

    elif opcao == '3':
        print('\n====== EXTRATO =====')
        print('Não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('======================')
    elif opcao == '4':
        break
    
    else:
        print('Operação inválida, por favor selecione a operação desejada.')