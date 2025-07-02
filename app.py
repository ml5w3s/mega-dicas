from flask import Flask, render_template, request, redirect, url_for
from parametros_estatisticos import gerar_numero
from validadores import possui_tres_ou_mais_consecutivos, possui_numeros_repetidos
from utils import ler_combinacoes_arquivo

app = Flask(__name__)
ARQUIVO_CSV = 'resultados_filtrados.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    combinacao = None
    erro = None
    fixos = []

    if request.method == 'POST':
        raw = request.form.getlist('numero')
        try:
            fixos = [int(v) for v in raw if v.strip() != '']
        except ValueError:
            erro = "Só são permitidos números inteiros de 1 a 60."
        else:
            if len(fixos) > 5:
                erro = "Insira no máximo 5 números."
            elif len(set(fixos)) != len(fixos):
                erro = "Números duplicados não são permitidos."
            elif any(n < 1 or n > 60 for n in fixos):
                erro = "Todos os números devem estar entre 1 e 60."

        if not erro:
            combinacao = gerar_combinacao_web(fixos)
            return render_template('index.html', combinacao=combinacao, fixos=fixos)

    return render_template('index.html', erro=erro, fixos=fixos)

def gerar_combinacao_web(fixos):
    existentes = ler_combinacoes_arquivo(ARQUIVO_CSV)

    while True:
        candidatos = fixos.copy()
        while len(candidatos) < 6:
            novo = gerar_numero()
            if novo not in candidatos:
                candidatos.append(novo)

        candidatos.sort()
        tpl = tuple(candidatos)

        if (
            tpl not in existentes and
            not possui_numeros_repetidos(tpl) and
            not possui_tres_ou_mais_consecutivos(tpl)
        ):
            return tpl

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
