# 107 & 108 & 109 & 110

def aumentar(preco, val, formatado=False):
    preco += (preco * val / 100)
    
    if formatado:
        return moeda(preco)
    else:
        return preco


def diminuir(preco, val, formatado=False):
    preco -= (preco * val / 100)

    if formatado:
        return moeda(preco)
    else:
        return preco


def dobro(preco, formatado=False):
    preco *= 2

    if formatado:
        return moeda(preco)
    else:
        return preco


def metade(preco, formatado=False):
    preco /= 2

    if formatado:
        return moeda(preco)
    else:
        return preco


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def resumo(preco, valMais, valMenos):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    print(f'{"Preço analisado:":<20}' + f'{moeda(preco)}')
    print(f'{"Dobro do preço:":<20}' + f'{dobro(preco, True)}')
    print(f'{"Metade do preço:":<20}' + f'{metade(preco, True)}')
    print(f'{f"{valMais}% de aumento:":<20}' + f'{aumentar(preco, valMais, True)}')
    print(f'{f"{valMenos}% de redução:":<20}' + f'{diminuir(preco, valMenos, True)}')

    print('-' * 30)