import sqlite3

class Banco():
    
    def __init__(self):
        self.__conn = self.__conexao()
        self.__cursor = self.__cursorBd()
        self.__banco = self.__createBD()
    
    def __conexao(self):
        return sqlite3.connect('banco.db')
    
    def __createBD(self):
        return self.__cursor.execute('create table if not exists contato(nome, endereco, telefone)')
        
    def __cursorBd(self):
        return self.__conn.cursor()
    
    def _execute(self):
        res = self.__cursor.execute('select name from sqlite_master')
        return print(res.fetchone())
    