# 094

dicionarios = []
idadeTotal = 0

while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    idadeTotal += idade

    dicionarios.append({'nome': nome, 'sexo': sexo, 'idade': idade})

    print('-=' * 15)

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    print('-=' * 15)
    if conf == 'n':
        break


print(f'— {len(dicionarios)} pessoas foram cadastradas.')

print(f'— A média de idade é de {idadeTotal / len(dicionarios):.1f} anos.')

print('— As mulheres cadastradas foram: ', end='')
for i in dicionarios:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print()

print('— Lista das pessoas que estão acima da média: ')
for i in dicionarios:
    if i['idade'] > (idadeTotal / len(dicionarios)):
        print(f'  nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}; ')

print('<< ENCERRADO >>')