# 004

valor = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(valor)))
print('Esse valor só tem espaços? {}'.format(valor.isspace()))
print('Esse valor é um número? {}'.format(valor.isnumeric()))
print('Esse valor é alfabético? {}'.format(valor.isalpha()))
print('Esse valor é alfanumérico? {}'.format(valor.isalnum()))
print('Esse valor está em maiúsculo? {}'.format(valor.isupper()))
print('Esse valor está em minúsculo? {}'.format(valor.islower()))
print('Esse valor está capitalizado? {}'.format(valor.istitle()))