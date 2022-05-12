# 071

val = 0
ced50, ced20, ced10, ced1 = 0, 0, 0, 0

print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40)

while True:
    while True:
        try:
            val = int(input('Qual valor você quer sacar? R$'))
        except ValueError:
            continue
        break

    ced50 = val // 50
    val -= (ced50 * 50)
    
    ced20 = val // 20
    val -= (ced20 * 20)

    ced10 = val // 10
    val -= (ced10 * 10)

    ced1 = val // 1
    val -= (ced1 * 1)

    if ced50 > 0:
        print(f'Total de {ced50} cédula(s) de R$50')

    if ced20 > 0:
        print(f'Total de {ced20} cédula(s) de R$20')

    if ced10 > 0:
        print(f'Total de {ced10} cédula(s) de R$10')
        
    if ced1 > 0:
        print(f'Total de {ced1} cédula(s) de R$1')

    print('=' * 40)
    print('Volte sempre ao Banco CEV! Tenha um bom dia!')

    break
