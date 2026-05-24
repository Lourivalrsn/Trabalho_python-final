from tkinter import *

#cria a janela
janela = Tk()

#nome do titulo
janela.title("E-sports Treinos")

#Tamanho da janela
janela.geometry("900x600")

#cor 
janela.config(bg="#1e1e1e")

#texto
titulo = Label(
    janela,
    text="E-sports Treino",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 24)  
)

titulo.pack(pady=20)

janela.mainloop()
