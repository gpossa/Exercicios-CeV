# 113

def lerInt(string):
    while True:
        try:
            inpt = int(input(string))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        except:
            print('Valor inválido.')
            continue
        
        return inpt


def lerFloat(string):
    while True:
        try:
            inpt = float(input(string))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        except:
            print('Valor inválido.')
            continue
        
        return inpt


i = lerInt('Digite um número inteiro: ')
f = lerFloat('Digite um número float: ')

print(f'Inteiro: {i} & Float: {f}.')
