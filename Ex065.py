# 065

resposta = 's'
media, count, numLst = 0, 0, []

while resposta == 's':
    num = int(input('Digite um número: '))
    count += 1
    media += num
    numLst.append(num)

    resposta = input('Quer continuar? [S/N] ').strip().lower()[0]

numLst.sort()

print(f'Você digitou {count} números. A média entre todos eles é {media / count}')
print(f'O menor número digitado foi {numLst[0]} e o maior {numLst[-1]}')
