#vamos criar um sistema bancário com opçoes de depósito, saque e extrato.
menu = """
===========================
    BANCO WAGNOPLA
___________________________
    Selecione a operação desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
===========================
=> """
saldo = 0
limite=500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower().strip()
    if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
                    print("\nDepósito realizado com sucesso!")
                    print(f"Saldo atual: R$ {saldo:.2f}")

                else:
                    print("\nOperação falhou! O valor do depósito deve ser positivo.")

            except ValueError:
           
                print("\nOperação falhou! Por favor, informe um valor numérico.")
  
    elif opcao == "s":
        print("Saque")
        try:
            valor = float(input(f"O seu saldo é de R$ {saldo:.2f}\n Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("\nOperação falhou! O valor do saque excede o limite por saque.")

            elif excedeu_saques:
                print("\nOperação falhou! Número máximo de saques diários excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("\nSaque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")

            else:
                print("\nOperação falhou! O valor do saque deve ser positivo.")

        except ValueError:
            print("\nOperação falhou! Por favor, informe um valor numérico.")

    elif opcao == "e":
            
            print("Extrato")
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
    
    elif opcao == "q":
        print("Obrigado por usar o Banco Wagnopla. Volte sempre!\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")