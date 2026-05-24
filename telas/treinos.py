from tkinter import *
from tkinter import ttk
import sqlite3
import os

# CAMINHO DO BANCO
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_banco = os.path.join(BASE_DIR, "esports.db")

# JANELA
janela = Tk()

janela.title("Registro de Treinos")
janela.geometry("700x500")

# TITULO
Label(
    janela,
    text="Registro de Treinos",
    font=("Arial",20)
).pack(pady=20)

# CAMPOS
Label(janela,text="Jogador").pack()
entry_jogador = Entry(janela,width=40)
entry_jogador.pack()

Label(janela,text="Horas").pack()
entry_horas = Entry(janela,width=40)
entry_horas.pack()

Label(janela,text="Data").pack()
entry_data = Entry(janela,width=40)
entry_data.pack()

Label(janela,text="Observação").pack()
entry_obs = Entry(janela,width=40)
entry_obs.pack()

# TABELA
tabela = ttk.Treeview(
    janela,
    columns=("id","jogador","horas","data"),
    show="headings"
)

tabela.heading("id", text="ID")
tabela.heading("jogador", text="Jogador")
tabela.heading("horas", text="Horas")
tabela.heading("data", text="Data")

tabela.pack(pady=20, fill="both", expand=True)

# CARREGAR TABELA
def carregar_tabela():

    for item in tabela.get_children():
        tabela.delete(item)

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id,jogador,horas,data
    FROM treinos
    """)

    dados = cursor.fetchall()

    for linha in dados:
        tabela.insert("", END, values=linha)

    conexao.close()

# SALVAR
def salvar():

    conexao = sqlite3.connect(caminho_banco)

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

    carregar_tabela()

# APAGAR
def apagar():

    item = tabela.selection()

    if item:

        valores = tabela.item(item[0], "values")

        id_treino = valores[0]

        conexao = sqlite3.connect(caminho_banco)

        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM treinos WHERE id=?",
            (id_treino,)
        )

        conexao.commit()
        conexao.close()

        carregar_tabela()
        
    # VOLTAR MENU

def voltar_menu():

    janela.destroy()

    
    # BOTÃO VOLTAR

Button(
    janela,
    text="Voltar ao Menu",
    bg="gray",
    fg="white",
    command=voltar_menu
).pack(pady=10)

# BOTÃO SALVAR
Button(
    janela,
    text="Salvar Treino",
    bg="green",
    fg="white",
    command=salvar
).pack(pady=10)

# BOTÃO APAGAR
Button(
    janela,
    text="Apagar Treino",
    bg="red",
    fg="white",
    command=apagar
).pack(pady=10)

# INICIAR
carregar_tabela()

janela.mainloop()