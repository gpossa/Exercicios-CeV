# 155

def cores(r, g, b, texto):
    return f'\033[38;2;{r};{g};{b}m{texto} \033[38;2;255;255;255m'

def linha():
    return '-' * 45

def cabeçalho(txt):
    return linha() + f'\n{txt:^45}\n' + linha()

def menu(*opcoes):
    print(cabeçalho('MENU PRINCIPAL'))

    for n, i in enumerate(opcoes):
        print(f'{cores(255, 235, 25, n + 1)} - {cores(25, 130, 255, i)}')
        
    print(linha())

def lerInt(txt, values = False, minVal = 0, maxVal = 0):
    var = 0

    while True:
        try:
            var = int(input((cores(255, 235, 25, txt))))
        except (ValueError, IndexError):
            print(mensagemErro())
            continue
        if values:
            if var < minVal or var > maxVal:
                print(mensagemErro())
                continue
        break

    return var

def lerStr(txt):
    var = ''

    while True:
        try:
            var = str(input(cores(255, 235, 25, txt))).strip().title()
        except IndexError:
            print(mensagemErro())
            continue
        if var == '':
            print(mensagemErro())
            continue
        break

    return var
    
def mensagemErro():
    return cores(255, 40, 25, 'Valor inválido. Tente novamente')