from tkinter import *
import os

# FUNÇÕES PARA ABRIR TELAS

def abrir_jogadores():
    os.system("python telas/jogadores.py")

def abrir_treinos():
    os.system("python telas/treinos.py")

def abrir_ranking():
    os.system("python telas/ranking.py")

# JANELA
janela = Tk()

janela.title("E-sports Manager")

janela.geometry("900x600")

janela.config(bg="#1e1e1e")

# TITULO
titulo = Label(
    janela,
    text="E-sports Manager",
    bg="#1e1e1e",
    fg="white",
    font=("Arial",30)
)

titulo.pack(pady=40)

# BOTÃO JOGADORES
botao_jogadores = Button(
    janela,
    text="Cadastro de Jogadores",
    width=30,
    height=2,
    bg="#4CAF50",
    fg="white",
    font=("Arial",12),
    command=abrir_jogadores
)

botao_jogadores.pack(pady=10)

# BOTÃO TREINOS
botao_treinos = Button(
    janela,
    text="Registro de Treinos",
    width=30,
    height=2,
    bg="#2196F3",
    fg="white",
    font=("Arial",12),
    command=abrir_treinos
)

botao_treinos.pack(pady=10)

# BOTÃO RANKING
botao_ranking = Button(
    janela,
    text="Ranking",
    width=30,
    height=2,
    bg="#FF9800",
    fg="white",
    font=("Arial",12),
    command=abrir_ranking
)

botao_ranking.pack(pady=10)

janela.mainloop()