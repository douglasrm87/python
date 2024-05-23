import sqlite3
from sqlite3 import Error
from tkinter import *

def conexaoBanco():
    con = None
    try:
        con = sqlite3.connect('banco.db')
    except Error as er:
        print(str(er))
    return con

def criartable(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        print("A Table foi criada com sucesso!")
    except Error as er:
        print(str(er))


def insert(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print("Insert feito com Sucesso!")
    except Error as er:
        print(str(er))


def select(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        conexao.commit()
        return result
    except Error as er:
        print(str(er))


xcon = conexaoBanco()

xsql = """CREATE TABLE seguro (
        SEGURO_PLACA VARCHAR(10) NOT NULL,
        SEGURO_MODELO VARCHAR(30) NOT NULL,
        SEGURO_IDADE INT NOT NULL,
        SEGURO_VALORBASE FLOAT NOT NULL
);"""

criartable(xcon, xsql)


def GravarDados():
    gravar = Tk()
    gravar.title("Gravação")
    gravar.geometry("300x200")
    gravar.configure(background="black")
    segurop = vplaca.get()
    segurom = vmodelo.get()
    seguroi = vidade.get()
    segurob = vbase.get()
    xsql = "INSERT INTO seguro (SEGURO_PLACA, SEGURO_MODELO,SEGURO_IDADE,SEGURO_VALORBASE) VALUES ('" + \
        segurop+"','"+segurom+"','"+seguroi+"','"+segurob+"')"
    insert(xcon, xsql)
    Label(gravar, text="Os dados foram inseridos com sucesso!",
          background="black", fg="#fff").place(x=30, y=30)
    gravar.mainloop()


def novajanela():
    novajanela = Tk()
    novajanela.title("Impressão")
    novajanela.geometry("200x400")
    novajanela.configure(background="black")
    parametro = vplaca.get()
    xsql = "SELECT * FROM seguro where `SEGURO_PLACA` = '"+parametro+"' "
    teste = select(xcon, xsql)
    for row in teste:
        a = (str((row[0])))
        b = (str((row[1])))
        c = (str((row[2])))
        d = (str((row[3])))
    txt1 = Label(novajanela, text="Placa(XXX-0000)",
                 background="black", fg="#fff")
    txt1.place(x=5, y=10)
    placa = Entry(novajanela)
    placa.place(x=10, y=40, width=150, height=25)
    txt2 = Label(novajanela, text="Modelo/Ano", background="black", fg="#fff")
    txt2.place(x=5, y=70)
    modelo = Entry(novajanela)
    modelo.place(x=10, y=97, width=150, height=25)
    txt3 = Label(novajanela, text="Idade", background="black", fg="#fff")
    txt3.place(x=5, y=130)
    idade = Entry(novajanela)
    idade.place(x=10, y=160, width=150, height=25)
    txt4 = Label(novajanela, text="Valor Base", background="black", fg="#fff")
    txt4.place(x=5, y=190)
    base = Entry(novajanela)
    base.place(x=10, y=215, width=150, height=25)
    placa.insert(50, a)
    modelo.insert(50, b)
    idade.insert(50, c)
    base.insert(50, d)
    novajanela.mainloop()


janela = Tk()
janela.title("Seguro")
janela.geometry("200x400")
janela.configure(background="black")

txt1 = Label(janela, text="Placa(XXX-0000)", background="black", fg="#fff")
txt1.place(x=5, y=10)
vplaca = Entry(janela)
vplaca.place(x=10, y=40, width=150, height=25)
txt2 = Label(janela, text="Modelo/Ano", background="black", fg="#fff")
txt2.place(x=5, y=70)
vmodelo = Entry(janela)
vmodelo.place(x=10, y=97, width=150, height=25)
txt3 = Label(janela, text="Idade", background="black", fg="#fff")
txt3.place(x=5, y=130)
vidade = Entry(janela)
vidade.place(x=10, y=160, width=150, height=25)
txt4 = Label(janela, text="Valor Base", background="black", fg="#fff")
txt4.place(x=5, y=190)
vbase = Entry(janela)
vbase.place(x=10, y=215, width=150, height=25)

btng = Button(janela, text="Gravar", command=GravarDados)
btng.place(x=10, y=250)

btnl = Button(janela, text="Listar p/Placa", command=novajanela)
btnl.place(x=70, y=250)

janela.mainloop()

