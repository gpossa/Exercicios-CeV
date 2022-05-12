# 040

nota = []

for index in range(2):
    element = float(input(f'Digite a {index + 1}º nota do aluno: '))
    nota.append(element)

media = (nota[0] + nota[1]) / 2

print(f'A média foi de: {media:<.1f}')

if media < 5.0:
    print('Reprovado!')

elif media > 5.0 and media < 6.9:
    print('Recuperação!')
    
else:
    print('Aprovado!')