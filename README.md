# PYSQL - Sistema de Gerenciamento de Clientes

Sistema desktop desenvolvido em Python para gerenciamento de clientes com interface gráfica Tkinter e banco de dados SQLite utilizando fielmente os conceitos de Programação Orientada a Objetos.

## 📋 Funcionalidades

- **Cadastro de Clientes**: Inserção de novos clientes com validação de dados
- **Visualização**: Listagem completa de todos os clientes cadastrados
- **Busca**: Pesquisa por nome, sobrenome, email ou CPF
- **Atualização**: Edição de dados de clientes existentes
- **Exclusão**: Remoção de registros do banco de dados
- **Interface Intuitiva**: GUI desenvolvida com Tkinter

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** - Interface gráfica
- **SQLite3** - Banco de dados
- **PyInstaller** - Geração de executável

## 📁 Estrutura do Projeto

```
projeto/
├── main.py                     # Arquivo principal
├── banco.db                    # Banco de dados SQLite
├── main.spec                   # Configuração PyInstaller
└── modules/
    ├── __init__.py
    ├── app.py                  # Classe principal da aplicação
    ├── classDatabase.py        # Gerenciamento do banco de dados
    ├── classTkinter.py         # Interface gráfica
    └── functions/
        ├── __init__.py
        ├── util.py             # Funções de validação
        └── test_util.py        # Testes unitários
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Bibliotecas padrão do Python (tkinter, sqlite3)

### Execução
```bash
cd projeto
python main.py
```

### Gerar Executável
```bash
pyinstaller main.spec
```

### Instale o executável 
- Baixe o zip main app na pasta /dist
- Seu Sistema Operacional irá avisá-lo de que o arquivo é potencialmente perigoso por questões de segurança, se quiser continuar, clique em "Executar mesmo assim" ou algo relacionado

## 💾 Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

**Tabela: clientes**
- `id` (INTEGER PRIMARY KEY) - Identificador único
- `nome` (TEXT) - Nome do cliente
- `sobrenome` (TEXT) - Sobrenome do cliente
- `email` (TEXT) - Email do cliente
- `cpf` (TEXT) - CPF do cliente

## ✅ Validações Implementadas

- **Nome/Sobrenome**: Não podem conter números
- **Email**: Deve conter o caractere '@'
- **CPF**: Deve ter exatamente 11 dígitos (aceita formatação com pontos e hífen)

## 🎯 Como Usar

1. **Inserir Cliente**: Preencha os campos e clique em "Inserir"
2. **Ver Todos**: Clique em "Ver Todos" para listar todos os clientes
3. **Buscar**: Preencha qualquer campo e clique em "Buscar"
4. **Editar**: Selecione um cliente na lista, edite os campos e clique em "Atualizar"
5. **Excluir**: Selecione um cliente na lista e clique em "Deletar"

## 🏗️ Arquitetura

### Classes Principais

- **App**: Classe principal que herda de Gui e Queries, gerencia a lógica da aplicação
- **Gui**: Responsável pela interface gráfica usando Tkinter
- **Banco**: Classe base para conexão e operações com SQLite
- **Queries**: Herda de Banco, implementa operações CRUD

### Padrões Utilizados

- **Herança Múltipla**: App herda de Gui e Queries
- **Encapsulamento**: Métodos e atributos privados/protegidos
- **Separação de Responsabilidades**: Interface, banco de dados e lógica separados

## 🧪 Testes

O projeto inclui testes unitários para validação de dados:

```bash
cd modules/functions
python -m unittest test_util.py
```

## 📝 Versão

**PYSQL Versão 1.3**

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/Afeature`)
3. Commit suas mudanças (`git commit -m 'Add some Afeature'`)
4. Push para a branch (`git push origin feature/Afeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto educacional para a Fundação Bradesco.
