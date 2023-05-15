def expect(input, expectedType, field):
    if isinstance(input, expectedType):
        return input
    raise AssertionError("Invalid input for type", field)

def validate_user_fields(payload):
    nome = payload.get('nome')
    login = payload.get('login')
    cep = str(payload.get('cep')).replace("-", "")
    numero = payload.get('numero', 0)
    complemento = payload.get('complemento', '')
    telefone = payload.get('telefone', 0)

    if not nome or len(nome) > 100:
        return ('Invalid or empty value for the "nome" field', payload)
    elif not login or len(login) > 100:
        return ('Invalid or empty value for the "login" field', payload)
    elif not cep or len(cep) > 8:
        return ('Invalid or empty value for the "cep" field', payload)
    elif complemento and len(complemento) > 100:
        return ('Character limit exceeded for the "complemento" field', payload)

    payload['cep'] = cep
    payload['numero'] = numero
    payload['complemento'] = complemento
    payload['telefone'] = telefone

    return (True, payload)


# Exemplo de uso:
nome = 'Fulano de Tal'
login = 'fulano123'
cep = '12345-678'
numero = '10'
complemento = 'Apto 123'
telefone = '987654321'

payload = {
    'nome': nome,
    'login': login,
    'cep': cep,
    'numero': numero,
    'complemento': complemento,
    'telefone': telefone
}
