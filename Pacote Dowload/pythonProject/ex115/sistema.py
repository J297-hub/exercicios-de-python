from ex115.libry.interface import *
from ex115.libry.arquivo import *
from time import sleep

arq= 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta= menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta ==2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome= str(input('Nome: '))
        idade= leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('SAINDO DO SISTEMA ATÉ LOGO....')
        break
    else:
        # Digitou uma opção errada no menu
        print('ERRO! digite uma opção válida!')
    sleep(2)



