# 009

arrNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = int(input('Digite a tabuada que quer saber: '))

for index in range(len(arrNum)):
    resultado = valor * arrNum[index]
    print('{} * {:>2} = {}'.format(valor, arrNum[index], resultado))
