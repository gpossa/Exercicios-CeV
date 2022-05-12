# 097

def escrever(txt):
    print('~' * (len(txt) + 4))
    print(' ', txt)
    print('~' * (len(txt) + 4))

texto = str(input('Digite o texto: '))

escrever(texto)