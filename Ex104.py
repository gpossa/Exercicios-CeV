# 104

def leiaInt(string):
    while True:
        i = str(input(string).strip())
        
        if i.isnumeric():
            return i
        else:
            print('ERRO! Valor inválido.')
            continue


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')


    