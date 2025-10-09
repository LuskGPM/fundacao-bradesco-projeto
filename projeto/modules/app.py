from .classTkinter import Gui
from .classDatabase import Queries

class App(Gui, Queries):
    def __init__(self):
        super().__init__()
    
    def _comandoViews(self):
        linhas = self._view()
        self._listarClientes.delete(0, 'end')
        for linha in linhas:
            self._listarClientes.insert('end', linha)
            
    def _comandoBusca(self):
        self._listarClientes.delete(0, 'end')
        comand_cpf = self._getCPF()
        comand_email = self._getEmail()
        linhas = self._search(
            nome = self.nome.get(),
            sobrenome= self.sobrenome.get(),
            email = comand_email.get(),
            cpf = comand_cpf.get()
        )
        
        for linha in linhas:
            self._listarClientes.insert('end', linha)
        
    def _comandoInsert(self):
        insert_cpf = self._getCPF()
        insert_email = self._getEmail()
        
        self._insert(
            nome = self.nome.get(),
            sobrenome = self.sobrenome.get(),
            email = insert_email.get(),
            cpf = insert_cpf.get()
        )
        self._comandoViews()
        
    def _comandoUpdate(self):
        upd_email = self._getEmail()
        upd_cpf = self._getCPF()
        
        self._update(
            id=selected[0],
            nome=self.nome.get(),
            sobrenome=self.sobrenome.get(),
            email=upd_email.get(),
            cpf=upd_cpf.get()
        )
        
        self._comandoViews()
        
    def _comandoDel(self):
        del_id = selected[0]
        self._delete(id=del_id)
        self._comandoViews()
    
    def getSelectedRow(self, event):
        global selected
        
        index = self._listarClientes.curselection()[0]
        selected = self._listarClientes.get(index)
        self._entNome.delete(0, 'end')
        self._entNome.insert('end', selected[1])
        self._entSobrenome.delete(0, 'end')
        self._entSobrenome.insert('end', selected[2])
        self._entEmail.delete(0, 'end')
        self._entEmail.insert('end', selected[3])
        self._entCpf.delete(0, 'end')
        self._entCpf.insert('end', selected[4])
        
        return selected
    
    def _configureButtons(self):
        self._btnViewAll.configure(command=self._comandoViews)
        self._btnBuscar.configure(command=self._comandoBusca)
        self._btnInserir.configure(command=self._comandoInsert)
        self._btnUpdate.configure(command=self._comandoUpdate)
        self._btnDel.configure(command=self._comandoDel)
        self._btnClose.configure(command=self._getJanela().destroy)
    
    def __constructApp(self):
        janela = self._getJanela()
        janela.wm_title('PYSQL Versão 1.2')
        self._createGrid()
        self._configureButtons()
        self._listarClientes.bind('<<ListboxSelect>>', self.getSelectedRow)
        self._comandoViews()
        
    def start(self):
        self.__constructApp()
        janela = self._getJanela()
        janela.mainloop()
