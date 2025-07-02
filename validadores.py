def possui_tres_ou_mais_consecutivos(combinacao):
    """
    Verifica se há 3 ou mais números consecutivos na combinação.
    Exemplo: (21, 22, 23, 45, 52, 59) => True
    """
    combinacao_ordenada = sorted(combinacao)
    consecutivos = 1
    for i in range(1, len(combinacao_ordenada)):
        if combinacao_ordenada[i] == combinacao_ordenada[i - 1] + 1:
            consecutivos += 1
            if consecutivos >= 3:
                return True
        else:
            consecutivos = 1
    return False


def possui_numeros_repetidos(combinacao):
    """
    Verifica se há números repetidos na combinação.
    """
    return len(set(combinacao)) != len(combinacao)
