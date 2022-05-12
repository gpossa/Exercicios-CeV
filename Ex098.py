# 098

from time import sleep

def contador(inicio, fim, passo):
    print('=-' * 20)
    
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim:
        for i in range(inicio, fim - 1, -(passo)):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)

    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('=-' * 20)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))

contador(inicio, fim, passo)