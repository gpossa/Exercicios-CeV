# 105

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param notas: Notas de alunos (aceita várias)
    :param sit: (Opcional) Mostrar ou não a situação
    :return: Dicionário com as informações referente as notas
    """
    media = sum(notas) / len(notas)

    if sit:
        if media < 6:
            situ = 'RUIM'
        elif media < 7:
            situ = 'RAZOÁVEL'
        else:
            situ = 'BOA'

        return {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': media, 'situação': situ}
    else:
        return {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'média': media}

resp = notas(3.5, 4, 6.5, sit=True)
print(resp)