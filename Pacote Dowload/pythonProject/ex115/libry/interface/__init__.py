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


def linha(tam=42):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[35m{c} - \033[34m{item}\033[m')
        c=c+1
    print(linha())
    opc=leiaInt('\033[32mSua opção: \033[m')
    return opc