# 022

nome = input('Digite o nome completo da pessoa: ')
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
numLetrasTotal = len(nome) - nome.count(' ')
numLetrasNome1 = len(nome.split()[0])

print('Em maíusculo: {} \nEm minúsculo: {} \nNúmero total de letras: {} \nNúmero de letras do primeiro nome: {}'.format(nomeMaiusculo, nomeMinusculo, numLetrasTotal, numLetrasNome1))
