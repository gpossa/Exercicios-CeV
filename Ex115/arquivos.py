# 115

try:
    f = open('Exercícios - Curso/Ex115/.ex115.txt', 'x+')
except FileExistsError:
    f = open('Exercícios - Curso/Ex115/.ex115.txt', 'r+')

def escrever(nome, idade):
    f.write(f'{nome},{idade}|')

def ler():
    f.seek(0)

    for line in f:
        for char in line.split('|'):
            try:
                print(f'{char.split(",")[0]:<35} {char.split(",")[1]} Anos')
            except:
                break