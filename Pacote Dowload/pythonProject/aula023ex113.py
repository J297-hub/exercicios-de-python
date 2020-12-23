def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VALIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;33mO usuário decidiu para a coleta de dados.\033[m')
            return 0
        else:
            return n


def leiaFloat(msn):
    while True:
        try:
            n = float(input(msn))
        except (TypeError, ValueError):
            print('\033[0;32mERRO! DIGITE UM NÚMERO REAL VALIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;35mO USUÁRIO DECIDIU ENCERRAR A COLETA DE DADOS.\033[m')
            return 0                # pra não dar laço infinito
        else:
            return n


# Programa Principal
a1 = leiaInt('Digite um número Inteiro: ')
a2 = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {a1} e o Real foi {a2}.')
