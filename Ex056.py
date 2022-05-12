# 056

idadeMedia = 0
idadeHomemVelho = 0
nomeHomemVelho =  ''
mulheresMenosDe20 = 0

for index in range(0, 4):
    nome = input(f'Digite o nome da {index + 1}º pessoa: ')
    idade = int(input(f'Digite a idade da {index + 1}º pessoa: '))
    sexo = input(f'Digite o sexo da {index + 1}º pessoa (M/F): ').strip().upper()
    print('-' * 20)

    idadeMedia += idade

    if sexo == 'M':
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade
            nomeHomemVelho = nome
            
    else:
        if idade < 20:
            mulheresMenosDe20 += 1


print(f'A idade média do grupo é: {idadeMedia / 4}.')
print(f'O homem mais velho é: {nomeHomemVelho} e tem: {idadeHomemVelho} anos.')
print(f'{mulheresMenosDe20} mulheres tem menos de 20 anos.')