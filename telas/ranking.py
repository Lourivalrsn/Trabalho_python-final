from tkinter import *
from tkinter import ttk
import sqlite3

janela = Tk()

janela.title("Ranking")

janela.geometry("600x400")

titulo = Label(
    janela,
    text="Ranking de Treinos",
    font=("Arial",20)
)

titulo.pack(pady=20)

# TABELA
tabela = ttk.Treeview(
    janela,
    columns=("jogador","horas"),
    show="headings"
)

tabela.heading("jogador", text="Jogador")
tabela.heading("horas", text="Total Horas")

tabela.pack(pady=20)

# DADOS
conexao = sqlite3.connect("esports.db")

cursor = conexao.cursor()

dados = cursor.execute("""
SELECT jogador,
SUM(CAST(horas AS INTEGER))
FROM treinos
GROUP BY jogador
ORDER BY SUM(CAST(horas AS INTEGER)) DESC
""")

for item in dados:
    tabela.insert("", END, values=item)

conexao.close()

janela.mainloop()