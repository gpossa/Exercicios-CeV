# 012

precoInicial = float(input('Qual o preço inicial do produto? R$'))
desconto = precoInicial * 0.05
precoFinal = precoInicial - desconto

print('O preço final do produto com 5% de desconto será R${:.2f}'.format(precoFinal))
