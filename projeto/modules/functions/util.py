def validarEntradas(nome:str, sobrenome:str, email:str, cpf:str) -> bool:
    
    if any(char.isdigit() for char in nome) or any(char.isdigit() for char in sobrenome):
        print('Nome ou sobrenome não pode conter números')
        return False
    
    elif '@' not in email:
        print('Email inválido')
        return False
    
    else:
        cpf_tratado = cpf.strip().replace('.', '').replace('-', '')
        if len(cpf_tratado) != 11:
            print('Tamanho do CPF inválido')
            return False
        try:
            cpf_tratado = int(cpf_int)
            return True
        except TypeError as t:
            print(f'Erro: {t}')
            return False