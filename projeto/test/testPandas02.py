import pandas as pd

def projetandoEstrutura():
    
    autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
    
    livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'Primeiras Estórias']
    
    ano = [2000, 2004, 2015, 2017]
    
    dados = {
        'Autor': autor,
        'Livro': livro,
        'Ano': ano
    }
    
    return pd.DataFrame(dados)

def toCSV():
    df = projetandoEstrutura()
    return df.to_csv('autores.csv')

autores = pd.read_csv('autores.csv', index_col=0)
print(autores)
print('-'*60)
print(autores.info())
print('-'*60)
print(autores.columns)
print('-'*60)
print(autores.index)