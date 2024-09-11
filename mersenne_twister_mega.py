import pandas as pd

# Carregar o arquivo CSV com os resultados da loteria
df = pd.read_csv('resultados_mega.csv')

# Definir as combinações que você deseja excluir
# Suponha que a coluna 'comb' contenha as combinações
comb_incluir = set([
    '10-15-23-34-45-50',
    '01-03-19-21-37-48'
])

# Função para verificar se uma combinação deve ser excluída
def deve_excluir(combinacao):
    return combinacao in comb_incluir

# Aplicar a função para filtrar o DataFrame
df_filtrado = df[~df['comb'].apply(deve_excluir)]

# Salvar o DataFrame filtrado em um novo arquivo CSV
df_filtrado.to_csv('resultados_filtrados.csv', index=False)

print('Combinações excluídas e resultados filtrados salvos em resultados_filtrados.csv')
