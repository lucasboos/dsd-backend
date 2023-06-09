def validate_user_fields(payload):
    nome = payload.get('nome')
    login = payload.get('login')
    cep = str(payload.get('cep')).replace("-", "")
    numero = payload.get('numero', 0)
    complemento = payload.get('complemento', '')
    telefone = payload.get('telefone', 0)

    if not nome or len(nome) > 100:
        return ('Valor inválido ou vazio para o campo "nome"', payload)
    elif not login or len(login) > 100:
        return ('Valor inválido ou vazio para o campo "login"', payload)
    elif not cep or len(cep) > 8:
        return ('Valor inválido ou vazio para o campo "cep"', payload)
    elif complemento and len(complemento) > 100:
        return ('Limite de caracteres excedido para o campo "complemento"', payload)

    payload['cep'] = cep
    payload['numero'] = numero
    payload['complemento'] = complemento
    payload['telefone'] = telefone

    return (True, payload)

def validate_cep_fields(payload):
    cep = str(payload.get('cep', '')).replace("-", "")
    payload['cep'] = cep

    ibge = payload.get('ibge', '')
    logradouro = payload.get('logradouro', '')
    bairro = payload.get('bairro', '')
    cidade = payload.get('cidade', '')
    uf = payload.get('uf', '')
    ddd = payload.get('ddd', '')

    if not ibge or len(str(ibge)) > 7:
        return ('O código do IBGE ultrapassou o limite de dígitos ou está vazio', payload)
    elif not cep or len(str(cep)) > 8:
        return ('O CEP ultrapassou o limite de dígitos ou está vazio', payload)
    elif not logradouro or len(str(logradouro)) > 100:
        return ('O logradouro ultrapassou o limite de caracteres ou está vazio', payload)
    elif len(str(bairro)) > 55:
        return ('O bairro ultrapassou o limite de caracteres', payload)
    elif not cidade or len(str(cidade)) > 100:
        return ('A cidade ultrapassou o limite de caracteres ou está vazia', payload)
    elif not uf or len(str(uf)) > 2:
        return ('A sigla da UF ultrapassou o limite de caracteres ou está vazia', payload)
    elif not ddd or len(str(ddd)) > 3:
        return ('O DDD ultrapassou o limite de caracteres ou está vazio', payload)

    ddd = payload.get('ddd', 0)

    payload['ddd'] = ddd

    return (True, payload)

def validate_cidade_fields(payload):
    cidade = payload.get('cidade', '')
    uf = payload.get('uf', '')
    ddd = payload.get('ddd', '')

    if not cidade or len(str(cidade)) > 100:
        return ('A cidade ultrapassou o limite de caracteres ou está vazia', payload)
    elif not uf or len(str(uf)) > 2:
        return ('A sigla da UF ultrapassou o limite de caracteres ou está vazia', payload)
    elif not ddd or len(str(ddd)) > 3:
        return ('O DDD ultrapassou o limite de caracteres ou está vazio', payload)

    ddd = payload.get('ddd', 0)

    payload['ddd'] = ddd

    return (True, payload)
