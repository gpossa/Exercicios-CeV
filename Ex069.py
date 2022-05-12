# 069

idade, pessoasMaiores, homensCadastrados, mulheresMenores = 0, 0, 0, 0
sexo, confirmacao = ' ', ' '

while True:
    print('-' * 40)
    print(('CADESTRE UMA PESSOA').center(40))
    print('-' * 40)

    while True:
        try:
            idade = int(input('Idade: ')) 
        except ValueError:
            continue
        break

    while True:
        try:
            sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
        except IndexError:
            continue
        if sexo not in 'mf':
            continue
        break

    print('-' * 40)

    if idade > 18:
        pessoasMaiores += 1

    if sexo == 'm':
        homensCadastrados += 1
    else:
        if idade < 20:
            mulheresMenores += 1

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

print('=' * 7, 'FIM DO PROGRAMA', '=' * 7)
print(f'Total de pessoas com mais de 18 anos: {pessoasMaiores}')
print(f'Total de homens cadastrados: {homensCadastrados}')
print(f'Total de mulheres com menos de 20 anos: {mulheresMenores}')