import tkinter as tk
from tkinter import messagebox
from parametros_estatisticos import encontrar_combinacao_unica
from utils import ler_combinacoes_arquivo

ARQUIVO_CSV = 'resultados_filtrados.csv'


class AppGeradorCombinacao:
    def __init__(self, master):
        self.master = master
        master.title("Gerador de Combinação Única")

        self.entradas = []

        tk.Label(master, text="Digite até 5 números (entre 1 e 60):").pack(pady=5)

        self.frame_entradas = tk.Frame(master)
        self.frame_entradas.pack()

        for _ in range(5):
            entrada = tk.Entry(self.frame_entradas, width=5, justify='center')
            entrada.pack(side='left', padx=2)
            self.entradas.append(entrada)

        self.botao_gerar = tk.Button(master, text="Gerar Combinação", command=self.gerar_combinacao)
        self.botao_gerar.pack(pady=10)

        self.resultado = tk.Label(master, text="", font=('Courier', 14), fg="blue")
        self.resultado.pack(pady=10)

    def gerar_combinacao(self):
        numeros_usuario = []

        for entrada in self.entradas:
            texto = entrada.get().strip()
            if texto:
                if not texto.isdigit():
                    return self.erro("Todos os valores devem ser números inteiros.")
                valor = int(texto)
                if not (1 <= valor <= 60):
                    return self.erro("Números devem estar entre 1 e 60.")
                if valor in numeros_usuario:
                    return self.erro("Números duplicados não são permitidos.")
                numeros_usuario.append(valor)

        if len(numeros_usuario) > 5:
            return self.erro("Digite no máximo 5 números.")

        try:
            combinacao_final = self.gerar_combinacao_com_base(numeros_usuario)
            texto_final = ' '.join(f"{n:02}" for n in combinacao_final)
            self.resultado.config(text=f"Combinação: {texto_final}")
        except Exception as e:
            self.erro(f"Erro ao gerar combinação: {e}")

    def gerar_combinacao_com_base(self, fixos):
        """Completa a combinação com os números do sistema."""
        combinacoes_existentes = ler_combinacoes_arquivo(ARQUIVO_CSV)

        from parametros_estatisticos import gerar_numero
        import random
        while True:
            candidatos = list(fixos)
            while len(candidatos) < 6:
                novo = gerar_numero()
                if novo not in candidatos:
                    candidatos.append(novo)

            candidatos_ordenados = tuple(sorted(candidatos))

            from validadores import (
                possui_tres_ou_mais_consecutivos,
                possui_numeros_repetidos
            )

            if (
                candidatos_ordenados not in combinacoes_existentes and
                not possui_tres_ou_mais_consecutivos(candidatos_ordenados) and
                not possui_numeros_repetidos(candidatos_ordenados)
            ):
                return candidatos_ordenados

    def erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)


if __name__ == '__main__':
    root = tk.Tk()
    app = AppGeradorCombinacao(root)
    root.mainloop()
