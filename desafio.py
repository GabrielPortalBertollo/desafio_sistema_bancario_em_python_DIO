menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
LIMITE_POR_SAQUE = 600
LIMITE_DE_DINHEIRO_SACADO_DIARIO = 1500
extrato = ""
numero_saques = 0
sacado=0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")



    elif opcao == "2":
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        limite_sacado_do_dia= sacado==LIMITE_DE_DINHEIRO_SACADO_DIARIO
        if excedeu_saques:
            print("Número diario máximo de saques excedido. Volte amanhã")
        elif limite_sacado_do_dia:
            print("Limite de valor sacado do dia atingido.")
        else:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > LIMITE_POR_SAQUE

            excedeu_limite_saque_diario= (valor+sacado)>LIMITE_DE_DINHEIRO_SACADO_DIARIO

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif valor > 0:
                fluxo = True
                if excedeu_limite_saque_diario:
                    excedente= (valor+sacado)-LIMITE_DE_DINHEIRO_SACADO_DIARIO
                    resposta = input(f"O valor excede o seu limite diario de saque, valor disponivel ${excedente:.2f}\n[1] Sacar ${excedente:.2f}\n[2] Cancelar saque\n==>")
                    if resposta=="1":
                        valor=excedente
                    else:
                        fluxo=False
                if fluxo:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    sacado += valor
                else:
                    print("Operação de saque cancelada")
            else:
                print("Operação falhou! O valor informado é inválido.")





    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")




    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")