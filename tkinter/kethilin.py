import tkinter as tk
import MySQLdb
from os import name, supports_bytes_environ
from typing import NamedTuple
import tkinter.messagebox as MessageBox
import sqlite3


con = MySQLdb.connect(host="localhost", database="av1", user="root", password="")

print("Conexão realizada",con)

try:
    
    cursor = con.cursor()
    criarTabela = 'CREATE TABLE seguro (id serial primary key, placa varchar (10), modelo varchar (10), idade int, valor varchar(20) )'
    cursor.execute(criarTabela)
    con.commit()
except Exception as e:
    print("Tabela já criada.")
    con.rollback()

class SuperLCasse:
    var = 0

class Demo1 (SuperClasse):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.placa = globals 
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = tk.Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.segundoContainer = tk.Frame(master)
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()      
        

        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(master)
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()

        self.quintoContainer = tk.Frame(master)
        self.quintoContainer["pady"] = 5
        self.quintoContainer.pack()

        self.sextoContainer = tk.Frame(master)
        self.sextoContainer["pady"] = 5
        self.sextoContainer.pack()

        self.setimoContainer = tk.Frame(master)
        self.setimoContainer["pady"] = 5
        self.setimoContainer.pack()

        self.titulo = tk.Label(self.primeiroContainer, text="Seguro")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()        

        self.placaLabel = tk.Label(self.segundoContainer,text="Placa(XXX-000): ", font=self.fontePadrao)
        self.placaLabel.pack()

        self.placa = tk.Entry(self.segundoContainer)
        self.placa["width"] = 22
        self.placa["font"] = self.fontePadrao
        self.placa.pack()
        

        self.modeloLabel = tk.Label(self.terceiroContainer, text="Modelo/Ano: ", font=self.fontePadrao)
        self.modeloLabel.pack()

        self.modelo = tk.Entry(self.terceiroContainer)
        self.modelo["width"] = 25
        self.modelo["font"] = self.fontePadrao
        self.modelo.pack()
        

        self.idadeLabel = tk.Label(self.quartoContainer, text="Idade: ", font=self.fontePadrao)
        self.idadeLabel.pack()

        self.idade = tk.Entry(self.quartoContainer)
        self.idade["width"] = 30
        self.idade["font"] = self.fontePadrao
        self.idade.pack()
        
        self.valorLabel = tk.Label(self.quintoContainer, text="Valor: ", font=self.fontePadrao)
        self.valorLabel.pack()

        self.valor = tk.Entry(self.quintoContainer)
        self.valor["width"] = 30
        self.valor["font"] = self.fontePadrao
        self.valor.pack()

        self.button1 = tk.Button(self.frame, text = 'Gravar', width = 25, command = self.gravar)
        self.button1.pack()
        self.button1["pady"] = 5
        self.frame.pack()
        
        self.button2 = tk.Button(self.frame, text = 'Listar', width = 25, command = self.pesquisar)
        self.button2.pack()
        self.button2["pady"] = 5

        self.frame.pack()

    def pesquisar(self):             
        if self.placa != "":
            con = MySQLdb.connect(host="localhost", database="av1", user="root", password="")
            #MODELO
            cursor = con.cursor()
            auxplaca = self.placa.get()
            dados = (auxplaca,)
            cursor.execute("SELECT modelo FROM seguro WHERE placa = %s", dados)          
            modelo = cursor.fetchone()   

            #IDADE
            cursor = con.cursor()
            auxplaca = self.placa.get()
            dados = (auxplaca,)
            cursor.execute("SELECT idade FROM seguro WHERE placa = %s", dados)          
            idade = cursor.fetchone()

            #VALOR
            cursor = con.cursor()
            auxplaca = self.placa.get()
            dados = (auxplaca,)
            cursor.execute("SELECT valor FROM seguro WHERE placa = %s", dados)          
            valor = cursor.fetchone()            

                    
            self.titulo1 = tk.Label(self.primeiroContainer, text="Modelo do carro")  
            self.titulo1["font"] = ("Arial", "10", "bold")
            self.titulo1.pack()     

            self.titulo2 = tk.Label(self.primeiroContainer, text=modelo)
            self.titulo2["font"] = ("Arial", "10", "bold")
            self.titulo2.pack()  

            self.titulo1 = tk.Label(self.primeiroContainer, text="Idade")  
            self.titulo1["font"] = ("Arial", "10", "bold")
            self.titulo1.pack()  
            self.titulo3 = tk.Label(self.primeiroContainer, text=idade)
            self.titulo3["font"] = ("Arial", "10", "bold")
            self.titulo3.pack()  

            self.titulo1 = tk.Label(self.primeiroContainer, text="Valor")  
            self.titulo1["font"] = ("Arial", "10", "bold")
            self.titulo1.pack()    
            self.titulo4 = tk.Label(self.primeiroContainer, text=valor)
            self.titulo4["font"] = ("Arial", "10", "bold")
            self.titulo4.pack()             




    def gravar(self):
        if self.placa.get () =="" or self.modelo.get() =="" or self.idade.get() =="" or self.valor.get() =="" :
            self.titulo = tk.Label(self.primeiroContainer, text="DADOS NÃO REGISTRADO FAVOR PREENCHA TODOS OS CAMPOS! :C")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()
        else:
            con = MySQLdb.connect(host="localhost", database="av1", user="root", password="")
            cursor = con.cursor()
            dados = (self.placa.get(), self.modelo.get(), self.idade.get(), self.valor.get())
            comando_SQL = 'INSERT INTO seguro (placa,modelo,idade,valor) VALUES (%s, %s, %s, %s)'
            cursor.execute(comando_SQL, dados)
            con.commit()
            
            self.titulo = tk.Label(self.primeiroContainer, text="DADOS REGISTADOS COM SUCESSO! :D")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()




class Listar (SuperClasse):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.segundoContainer = tk.Frame(master)
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.placaLabel = tk.Label(self.segundoContainer,text="Pesquisar Placa")
        self.placaLabel.pack()

        self.placa = tk.Entry(self.segundoContainer)
        self.placa["width"] = 22
        self.placa.pack()

        self.buttonpesquisa = tk.Button(self.frame, text = 'Pesquisar', width = 25, command = self.pesquisar)
        self.buttonpesquisa.pack()
        self.buttonpesquisa["pady"] = 5
        self.frame.pack()

    

 


def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()