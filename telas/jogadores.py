from tkinter import *
from tkinter import ttk
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

caminho_banco = os.path.join(BASE_DIR, "esports.db")

# JANELA
janela = Tk()

janela.title("Cadastro de Jogadores")

janela.geometry("700x500")

# TITULO
titulo = Label(
    janela,
    text="Cadastro de Jogadores",
    font=("Arial",20)
)

titulo.pack(pady=10)

# NOME
Label(janela, text="Nome").pack()

entry_nome = Entry(janela, width=40)
entry_nome.pack()

# NICKNAME
Label(janela, text="Nickname").pack()

entry_nick = Entry(janela, width=40)
entry_nick.pack()

# JOGO
Label(janela, text="Jogo").pack()

entry_jogo = Entry(janela, width=40)
entry_jogo.pack()

# NIVEL
Label(janela, text="Nivel").pack()

entry_nivel = Entry(janela, width=40)
entry_nivel.pack()

# FUNÇÃO CARREGAR TABELA

def carregar_tabela():

    for item in tabela.get_children():
        tabela.delete(item)

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    dados = cursor.execute("""
    SELECT id,nome,nickname,jogo,nivel
    FROM jogadores
    """)

    for jogador in dados:
        tabela.insert("", END, values=jogador)

    conexao.close()

# FUNÇÃO SALVAR

def salvar():

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO jogadores(nome,nickname,jogo,nivel)
    VALUES(?,?,?,?)
    """,(
        entry_nome.get(),
        entry_nick.get(),
        entry_jogo.get(),
        entry_nivel.get()
    ))

    conexao.commit()

    conexao.close()

    carregar_tabela()

    print("Jogador salvo")
    
    entry_nome.delete(0, END)
    entry_nick.delete(0, END)
    entry_jogo.delete(0, END)
    entry_nivel.delete(0, END)

# FUNÇÃO APAGAR

# FUNÇÃO APAGAR

def apagar():

    selecionado = tabela.selection()

    if selecionado:

        item = selecionado[0]

        valores = tabela.item(item, "values")

        id_jogador = valores[0]

        conexao = sqlite3.connect(caminho_banco)

        cursor = conexao.cursor()

        cursor.execute("""
        DELETE FROM jogadores
        WHERE id = ?
        """, (id_jogador,))

        conexao.commit()

        conexao.close()

        carregar_tabela()

        print("Jogador apagado")
        
        
        
    # FUNÇÃO VOLTAR
def voltar_menu():

    janela.destroy()

    
# BOTÃO VOLTAR

botao_voltar = Button(
    janela,
    text="Voltar ao Menu",
    bg="gray",
    fg="white",
    command=voltar_menu
)

botao_voltar.pack(pady=10)

# BOTÃO SALVAR

botao = Button(
    janela,
    text="Salvar Jogador",
    bg="green",
    fg="white",
    command=salvar
)

botao.pack(pady=10)

# BOTÃO APAGAR

botao_apagar = Button(
    janela,
    text="Apagar Jogador",
    bg="red",
    fg="white",
    command=apagar
)

botao_apagar.pack(pady=10)

# TABELA

tabela = ttk.Treeview(
    janela,
    columns=("id","nome","nick","jogo","nivel"),
    show="headings",
    selectmode="browse"
)

tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("nick", text="Nickname")
tabela.heading("jogo", text="Jogo")
tabela.heading("nivel", text="Nivel")

tabela.pack(pady=20, fill="both", expand=True)

# CARREGAR DADOS

carregar_tabela()

janela.mainloop()
