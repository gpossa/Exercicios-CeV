# 106

from time import sleep

def cores(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"

def cabeçalho(txt):
    linha = '=' * (len(txt) + 4)
    return (linha + (f'\n  {txt}  \n') + linha)

def ajuda():
    while True:      
        comando = str(input(cores(80, 170, 50, 'Função ou biblioteca > '))).strip().lower()
        if comando == 'fim':
            print(cores(255, 0, 0, cabeçalho('ENCERRANDO PROGRAMA')))
            break
        
        print(cores(120, 225, 80, cabeçalho(f'Acessando o Manual do Comando "{comando}"')))
        sleep(0.5)

        help(comando)
    
    
print(cores(80, 170, 50, cabeçalho('SISTEMA DE AJUDA PyHELP')))

ajuda()