# 090

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
else:
    aluno['situaçao'] = 'Reprovado'

print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["situaçao"]}')