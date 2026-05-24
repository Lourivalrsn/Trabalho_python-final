from tkinter import *
from tkinter import ttk
import sqlite3

#JANELA
janela = Tk()

janela.title("Cadastro de Jogadores")
janela.geometry("700x500")

#TITULO
titulo = Label(
    janela,
    text="Cadastro de Jogadores",
    font=("Arial",20)
)

titulo.pack(pady=10)

#NOME
Label(janela, text="Nome").pack()

entry_nome = Entry(janela, width=40)
entry_nome.pack()

#NICKNAME
Label(janela, text="Nickname").pack()

entry_nick = Entry(janela, width=40)
entry_nick.pack()

#JOGO
Label(janela, text="Jogo").pack()

entry_jogo = Entry(janela, width=40)
entry_jogo.pack()

#NIVEL
Label(janela, text="Nivel").pack()

entry_nivel = Entry(janela, width=40)
entry_nivel.pack()

#FUNÇÃO SALVAR
def salvar():

    conexao = sqlite3.connect("esports.db")

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

    print("Jogador salvo")

#BOTÃO
botao = Button(
    janela,
    text="Salvar Jogador",
    command=salvar
)

botao.pack(pady=10)

janela.mainloop()
#TABELA
tabela = ttk.Treeview(
    janela,
    columns=("nome","nick","jogo","nivel"),
    show="headings"
)

tabela.heading("nome", text="Nome")
tabela.heading("nick", text="Nickname")
tabela.heading("jogo", text="Jogo")
tabela.heading("nivel", text="Nivel")

tabela.pack(pady=20)

#MOSTRAR DADOS
conexao = sqlite3.connect("esports.db")

cursor = conexao.cursor()

dados = cursor.execute("""
SELECT nome,nickname,jogo,nivel
FROM jogadores
""")

for jogador in dados:
    tabela.insert("", END, values=jogador)

conexao.close()