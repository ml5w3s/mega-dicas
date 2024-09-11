import random
import csv

pesos = {10: 5, 53: 5, 5: 5, 34: 5, 42: 5, 37: 5, 4: 5, 23: 5, 51: 5}
faixa_preferida = set(range(30, 51))
preferencia_pares = 0.1


def gerar_numero():
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


def ler_combinacoes_arquivo(arquivo_csv):
    combinacoes = []
    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            numeros = [numero.strip() for numero in ' '.join(linha).split()]
            combinacoes.append(tuple(map(int, numeros)))
    return combinacoes


def gerar_combinacao_aleatoria():
    return tuple(sorted(gerar_numero() for _ in range(6)))


def encontrar_combinacao_unica(arquivo_csv):
    combinacoes_existentes = ler_combinacoes_arquivo(arquivo_csv)
    while True:
        nova_combinacao = gerar_combinacao_aleatoria()
        if nova_combinacao not in combinacoes_existentes:
            return nova_combinacao


arquivo_csv = 'resultados_filtrados.csv'
combinacao_unica = encontrar_combinacao_unica(arquivo_csv)
print("Combinação única gerada:", combinacao_unica)
