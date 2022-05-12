# 077

tup = ('gabriel', 'esta', 'aprendendo', 'python', 'jogar', 'bola', 'altofalante', 'aviao')

for index in tup:
    print(f'\nNa palavra {index.upper()} temos ', end='')
    
    for letra in index:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

        