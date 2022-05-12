# 070

nome, nomeBarato, confirmacao = '', '', ''
count, preco, precoBarato, precoTotal, qntMil = 0, 0, 0, 0, 0

print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40)

while True:
    while True:
        try:
            nome = str(input('Nome do produto: ')).strip()
        except IndexError:
            continue
        break

    while True:
        try:
            preco = float(input('Preço do produto: R$'))
        except ValueError:
            continue
        break
    
    count += 1
    precoTotal += preco

    if preco > 1000:
        qntMil += 1

    if count == 1:
        precoBarato = preco
        nomeBarato = nome
    else:    
        if preco < precoBarato:
            precoBarato = preco
            nomeBarato = nome

    print('-' * 40)

    while True:
        try:
            confirmacao = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        except IndexError:
            continue
        if confirmacao not in 'sn':
            continue
        break


    if confirmacao == 'n':
        break

    print('-' * 40)

print('=' * 7, 'FIM DO PROGRAMA', '=' * 7)
print(f'O total da compra foi de R${precoTotal:<.2f}')
print(f'Temos {qntMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${precoBarato:<.2f}')


