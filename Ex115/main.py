# 115

import arquivos
from time import sleep
from formatacao import cabeçalho, menu, lerInt, lerStr

while True: 
    menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    
    opcao = lerInt('Sua opção:', True, 1, 3)
    
    match opcao:
        case 1:
            print(cabeçalho('PESSOAS CADASTRADAS'))
            arquivos.ler()
            sleep(1)

        case 2:
            print(cabeçalho('NOVO CADASTRO'))

            nome = lerStr('Nome:')
            idade = lerInt('Idade:')

            arquivos.escrever(nome, idade)
            print(f'Novo registro de {nome} adicionado.')
            sleep(1)

        case 3:
            print(cabeçalho('>> VOLTE SEMPRE <<'))
            sleep(1)
            break

arquivos.f.close()