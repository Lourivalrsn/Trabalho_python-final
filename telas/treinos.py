from tkinter import *
from tkinter import ttk
import sqlite3

janela = Tk()

janela.title("Registro de Treinos")

janela.geometry("500x400")

Label(
    janela,
    text="Registro de Treinos",
    font=("Arial",20)
).pack(pady=20)

# JOGADOR
Label(janela,text="Jogador").pack()

entry_jogador = Entry(janela,width=40)
entry_jogador.pack()

# HORAS
Label(janela,text="Horas").pack()

entry_horas = Entry(janela,width=40)
entry_horas.pack()

# DATA
Label(janela,text="Data").pack()

entry_data = Entry(janela,width=40)
entry_data.pack()

# OBS
Label(janela,text="Observação").pack()

entry_obs = Entry(janela,width=40)
entry_obs.pack()

# SALVAR
def salvar():

    conexao = sqlite3.connect("esports.db")

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO treinos(
    jogador,horas,data,observacao
    )
    VALUES(?,?,?,?)
    """,(
        entry_jogador.get(),
        entry_horas.get(),
        entry_data.get(),
        entry_obs.get()
    ))

    conexao.commit()

    conexao.close()

    print("Treino salvo")

Button(
    janela,
    text="Salvar Treino",
    command=salvar
).pack(pady=20)

# TABELA

tabela = ttk.Treeview(
    janela,
    columns=("jogador","horas","data","obs"),
    show="headings"
)

tabela.heading("jogador", text="Jogador")
tabela.heading("horas", text="Horas")
tabela.heading("data", text="Data")
tabela.heading("obs", text="Observação")

tabela.pack(pady=20)

# MOSTRAR TREINOS

conexao = sqlite3.connect("esports.db")

cursor = conexao.cursor()

dados = cursor.execute("""
SELECT jogador,horas,data,observacao
FROM treinos
""")

for treino in dados:
    tabela.insert("", END, values=treino)

conexao.close()

janela.mainloop()
