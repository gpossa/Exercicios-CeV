# 010

brl = float(input('Quantos R$ você tem na carteira? R$'))
usd = 3.27
usdTotal = brl / usd

print('Com R${} você pode comprar US${:.2f} (cotação a US${})'.format(brl, usdTotal, usd))