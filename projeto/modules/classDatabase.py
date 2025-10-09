import sqlite3 as sql
from .functions import *

class Banco():
    def __init__(self):
        self.__conexao = None
        self.__cursor = None
        self.__conectado = False
    
    def _getConexao(self):
        return self.__conexao
    
    def _getCursor(self):
        return self.__cursor
        
    def _conectar(self):
        self.__conexao = sql.connect('banco.db')
        self.__cursor = self.__conexao.cursor()
        self.__conectado = True
        
    def _disconectar(self):
        self.__conexao.close()
        self.__conectado = False
        
    def _execute(self, sql, parametros = None):
        if self.__conectado:
            if parametros == None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql, parametros)
        else:
            return False
        
    def _fetchAll(self):
        return self.__cursor.fetchall()
    
    def _comitar(self):
        try:
            self.__conexao.commit()
        except sql.Error as e:
            print(e)
            return False

class Queries(Banco):
    def __init__(self):
        super().__init__()
        
    def iniciarBanco(self):
        self._conectar()
        self._execute('create table if not exists clientes (id integer primary key, nome text, sobrenome text, email text, cpf text)')
        self._comitar()
        self._disconectar()
        
    def _insert(self, nome:str, sobrenome:str, email:str, cpf:str):
        if validarEntradas(nome, sobrenome, email, cpf):    
            self._conectar()
            self._execute('insert into clientes (nome, sobrenome, email, cpf) values (?, ?, ?, ?)', (nome.strip(), sobrenome.strip(), email.strip(), cpf.strip()))
            self._comitar()
            self._disconectar()
        else:
            return 'Dados inválidos'
        
    def _view(self):
        self._conectar()
        self._execute('select * from clientes')
        linhas = self._fetchAll()
        self._disconectar()
        return linhas
        
    def _search(self, nome:str = '', sobrenome:str = '', email:str = '', cpf:str = ''):
        self._conectar()
        self._execute('select * from clientes where nome like ? or sobrenome like ? or email = ? or cpf = ?', (nome.strip(), sobrenome.strip(), email.strip(), cpf.strip()))
        linhas = self._fetchAll()
        self._disconectar()
        return linhas
        
    def _delete(self, id:int):
        self._conectar()
        self._execute('delete from clientes where id = ?', (id,))
        self._comitar()
        self._disconectar()
        
    def _update(self, id:int, nome:str, sobrenome:str, email:str, cpf:str):
        if validarEntradas(nome, sobrenome, email, cpf):
            self._conectar()
            self._execute('update clientes set nome = ?, sobrenome = ?, email = ?, cpf = ? where id = ?', (nome, sobrenome, email, cpf, id))
            self._comitar()
            self._disconectar()
            
        else:
            return 'Dados inválidos'
