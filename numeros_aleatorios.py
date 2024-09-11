import random
import csv

def gerar_numero():
    """Gera um número aleatório entre 1 e 60 com preferência para 10 a 50."""
    if random.random() < 0.6:  # 60% de chance de estar entre 10 e 50
        return random.randint(10, 50)
    else:
        return random.randint(1, 60)

def ler_combinacoes_arquivo(arquivo_csv):
    """Lê o arquivo CSV e retorna uma lista de combinações de números."""
    combinacoes = []
    with open(arquivo_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            # Remove espaços extras e divide a linha com base em espaços
            numeros = [numero.strip() for numero in ' '.join(linha).split()]
            # Converte cada número para inteiro e adiciona à lista
            combinacoes.append(tuple(map(int, numeros)))
    return combinacoes

def gerar_combinacao_aleatoria():
    """Gera uma combinação aleatória de 6 números inteiros."""
    return tuple(sorted(gerar_numero() for _ in range(6)))

def encontrar_combinacao_unica(arquivo_csv):
    """Encontra uma combinação de 6 números que não esteja no arquivo CSV."""
    combinacoes_existentes = ler_combinacoes_arquivo(arquivo_csv)
    while True:
        nova_combinacao = gerar_combinacao_aleatoria()
        if nova_combinacao not in combinacoes_existentes:
            return nova_combinacao

# Nome do arquivo CSV
arquivo_csv = 'resultados_filtrados.csv'

# Encontrar uma combinação única
combinacao_unica = encontrar_combinacao_unica(arquivo_csv)
print("Combinação única gerada:", combinacao_unica)
