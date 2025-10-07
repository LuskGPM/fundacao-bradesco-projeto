import pandas as pd

def linha() -> str:
    return print('--'*30)

#banco_instancia._execute()
#objSerie = pd.Series([1, 7, 9, 13, 17, 99])

disciplinas = {
    'cursos': ['estatistica', 't.i', 'economia', 'calculo'],
    'credito': [90, 60, 90, 40],
    'requisito': [True, False, True, False]
}

data_frame = pd.DataFrame(disciplinas)

nome_cidade = pd.Series(['Maringá', 'Itabira', 'Limoeiro'])
populacaoSerie = pd.Series([403.063, 120.904, 55.210])

cidadesZip = ['Maringá', 'Itabira', 'Uberlândia', 'Salvador', 'Fortaleza']
populacaoZip = [403.063, 120.904, 699.097, 2.886698, 2.686612]

populacao_cidades = dict(zip(cidadesZip, populacaoZip))
populacao_cidades['Vitória'] = 365.855

linha()
print(data_frame)
linha()
print(pd.DataFrame({'Cidade': nome_cidade, 'População': populacaoSerie}))
print(populacao_cidades)
print('Maringá' in populacao_cidades)
print(populacao_cidades['Vitória'])
linha()