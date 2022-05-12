# 102

def fatorial(num, show = False):
    """
    -> Calcula o fatorial de um número:
    :param n: O número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: O fatorial de num
    """
    fat = 1

    for i in range(num, 0, -1):
        fat *= i

        if show:
            if i > 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')
    
    return fat
            
print(fatorial(5, True))