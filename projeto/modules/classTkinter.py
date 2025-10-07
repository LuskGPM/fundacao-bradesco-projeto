from tkinter import *

class Gui():
    def __init__(self):
        self._xPad = 5
        self._yPad = 3
        self._widthEntry = 30
        self.__janela = Tk()
        
        self.nome = StringVar()
        self.sobrenome = StringVar()
        self.__email = StringVar()
        self.__cpf = StringVar()
        
    def __getCPF(self):
        return self.__cpf
        
    def __getEmail(self):
        return self.__email
    
    def __getJanela(self):
        return self.__janela
        
    def __createObjects(self):
        janela = self.__getJanela()
        
        # Labels
        
        self.__labelNome = Label(janela, text='Nome')
        self.__labelSobrenome = Label(janela, text='Sobrenome')
        self.__labelEmail = Label(janela, text='Email')
        self.__labelCpf = Label(janela, text='CPF')
        
        # Entradas
        
        self.__entNome = Entry(janela, textvariable=self.nome, width=self._widthEntry)
        self.__entSobrenome = Entry(janela, textvariable=self.sobrenome, width=self._widthEntry)
        email = self.__getEmail()
        self.__entEmail = Entry(janela, textvariable=email, width=self._widthEntry)
        cpf = self.__getCPF()
        self.__entCpf = Entry(janela, textvariable=cpf, width=self._widthEntry)
        
        # Funcionalidades
        
        self.__listarClientes = Listbox(janela, width=100)
        self.__scrollClientes = Scrollbar(janela)
        self.__btnViewAll = Button(janela, text='Ver Todos')
        self.__btnBuscar = Button(janela, text='Buscar')
        self.__btnInserir = Button(janela, text='Inserir')
        self.__btnUpdate = Button(janela, text='Atualizar')
        self.__btnDel = Button(janela, text='Deletar')
        self.__btnClose = Button(janela, text='Fechar')
        
    def __scrollWithListBox(self):
        self.__listarClientes.configure(yscrollcommand=self.__scrollClientes.set)
        self.__scrollClientes.configure(command=self.__listarClientes.yview)
        
    def __swag(self):
        janela = self.__getJanela()
        
        for filho in janela.winfo_children():
            widget_class = filho.__class__.__name__
            
            if widget_class == 'Button':
                filho.grid_configure(sticky='WE', padx=self._xPad, pady=self._yPad)
            
            elif widget_class == 'ListBox' or widget_class == 'Scollbar':
                filho.grid_configure(padx=0, pady=0, sticky='NS')
                
            else:
                filho.grid_configure(padx=self._xPad, pady=self._yPad, sticky='N')
            
        
    def __createGrid(self):
        
        self.__createObjects()
        
        self.__labelNome.grid(row=0, column=0)
        self.__labelSobrenome.grid(row=1, column=0)
        self.__labelEmail.grid(row=2, column=0)
        self.__labelCpf.grid(row=3, column=0)
        
        self.__entNome.grid(row=0, column=1, padx=50, pady=50)
        self.__entSobrenome.grid(row=1, column=1)
        self.__entEmail.grid(row=2, column=1)
        self.__entCpf.grid(row=3, column=1)
        
        self.__listarClientes.grid(row=0, column=2, rowspan=10)
        self.__scrollClientes.grid(row=0, column=6, rowspan=10)
        self.__btnViewAll.grid(row=4, column=0, columnspan=2)
        self.__btnBuscar.grid(row=5, column=0, columnspan=2)
        self.__btnInserir.grid(row=6, column=0, columnspan=2)
        self.__btnUpdate.grid(row=7, column=0, columnspan=2)
        self.__btnDel.grid(row=8, column=0, columnspan=2)
        self.__btnClose.grid(row=9, column=0, columnspan=2)
        
        # Liga o Scoll na Lista
        
        self.__scrollWithListBox()
        
        # Estiliza
        
        self.__swag()
    
    def start(self):
        janela = self.__getJanela()
        janela.wm_title('PYSQL Versão 1.0')
        self.__createGrid()
        janela.mainloop() 
        
