import random
from utils import ler_combinacoes_arquivo
from validadores import possui_tres_ou_mais_consecutivos, possui_numeros_repetidos

# Parâmetros estatísticos
pesos = {10: 5, 53: 5, 5: 5, 34: 5, 42: 5, 37: 5, 4: 5, 23: 5, 51: 5}
faixa_preferida = set(range(10, 50))
preferencia_pares = 0.1


def gerar_numero():
    """
    Gera um número entre 1 e 60 baseado em pesos personalizados,
    preferência por faixa e preferência por números pares.
    """
    numeros = list(range(1, 61))
    probabilidades = []

    for numero in numeros:
        peso = pesos.get(numero, 1)

        if numero in faixa_preferida:
            peso *= 1.2

        if numero % 2 == 0:
            peso *= (1 + preferencia_pares)

        probabilidades.append(peso)

    total_peso = sum(probabilidades)
    probabilidades = [p / total_peso for p in probabilidades]

    return random.choices(numeros, weights=probabilidades, k=1)[0]


def gerar_combinacao_aleatoria():
    """
    Gera uma combinação aleatória de 6 números com ordenação.
    """
    combinacao = []
    while len(combinacao) < 6:
        numero = gerar_numero()
        if numero not in combinacao:
            combinacao.append(numero)
    return tuple(sorted(combinacao))


def encontrar_combinacao_unica(arquivo_csv):
    """
    Encontra uma combinação única que:
    - Não está no arquivo
    - Não possui 3+ números consecutivos
    - Não possui números repetidos
    """
    combinacoes_existentes = ler_combinacoes_arquivo(arquivo_csv)

    while True:
        nova_combinacao = gerar_combinacao_aleatoria()

        if (
            nova_combinacao not in combinacoes_existentes and
            not possui_tres_ou_mais_consecutivos(nova_combinacao) and
            not possui_numeros_repetidos(nova_combinacao)
        ):
            return nova_combinacao


# Execução principal
if __name__ == '__main__':
    arquivo_csv = 'resultados_filtrados.csv'
    combinacao_unica = encontrar_combinacao_unica(arquivo_csv)
    print("Combinação única gerada:", combinacao_unica)
