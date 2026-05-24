import sqlite3

#conectar
conexao = sqlite3.connect("esports.db")

cursor = conexao.cursor()

#tabela de jogadores 
cursor.execute(""" 
    create table if not exists jogadores(
        id integer primary key autoincrement,
        nome text,
        nickname text,
        jogo text,
        nivel text)
    """)

#tabela  de treinos
cursor.execute(""" 
    create table if not exists treinos(
        id integer primary key autoincrement,
        jogador text,
        horas text,
        data text,
        observacao text)
    """)

conexao.commit()
conexao.close()

print("banco criado com sucesso")
