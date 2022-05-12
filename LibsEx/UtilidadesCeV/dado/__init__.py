# 112

def lerDinheiro(inpt):
    while True:
        valor = str(input(inpt)).strip().replace(',', '.')

        try:
            float(valor)
            return float(valor)
        except ValueError:
            print(f'ERRO! Preço "{valor}" é inválido.')
            continue