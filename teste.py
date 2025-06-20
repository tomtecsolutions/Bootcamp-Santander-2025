while True:
        valor = int(input("Insira o valor do saque:"))
        if valor > 0:
            valor_formatado = "{:.2f}".format(valor)
            print(f'Deposito realizado com sucesso!\nSaldo atual: R$',valor_formatado)
            break
        elif valor < 0:
            print('Valor invalido! Digite um valor maior que zero.')
        else:
            print('Encerrando o programa...')
            break