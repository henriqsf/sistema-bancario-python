menu = """

[d] Depositar
[s] Sacar
[e] Gerar Extrato
[q] Sair

= > """

saldo = 300
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_DEPOSITO = 1

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira o valor que deseja depositar: \n"))

        if deposito >= LIMITE_DEPOSITO:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("\nDepósito concluído! Seu saldo atual é: R$ {:.2f}".format(saldo))

        elif deposito < LIMITE_DEPOSITO:
            print("\nSó é possivel depositar valores a partir de R$ 1,00. \nPor favor tente novamente com um valor permitido.")

        else:
            print("\nValor Invalido! \nNão foi possivel completar a operação, por favor tente novamente!")

    elif opcao == "s":
        saque = float(input("\nInsira o valor que deseja sacar: \n"))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_saque
        excedeu_saques = numero_saques >= 3


        if saque <= saldo and saque < limite_saque and saque > 0 and numero_saques < 3:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("\nSaque concluído! Seu saldo atual é: R$ {:.2f}".format(saldo)) 

        elif excedeu_limite:
            print("\nValor de saque excedeu o limite permitido de R$ {:.2f}. \nTente novamente com um valor dentro do limite.".format(limite_saque))

        elif excedeu_saques:
            print("\nLimite de saques diarios atingido. \nTente novamente amanhã.")

        elif excedeu_saldo:
            print("\nSaldo insuficiente. \nTente novamente com um valor inferior.")

        else:
            print("\nValor Invalido! \nNão foi possivel completar a operação, por favor tente novamente!")

    elif opcao == "e":

        print("\n================== EXTRATO ==================\n")
        print("Não existe registro de transações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n=============================================")

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione uma operação valida.")
    
        

    