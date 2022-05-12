# 057

sexo = ''

sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]

while sexo not in 'MF':
        sexo = input('Sexo inválido. Digite seu sexo novamente [M/F]: ').strip().upper()[0]

print(f'Sexo {sexo} registrado.')
