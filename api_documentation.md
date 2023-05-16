# Documentação da API

## Endpoint - CEP

`POST /api/v1/cep/`

Esta API permite adicionar um novo CEP ao sistema.


## Parâmetros da Solicitação

A solicitação deve ser feita no formato JSON e deve conter os seguintes campos:

- `cep` (obrigatório): CEP numérico de 8 dígitos.
- `logradouro` (obrigatório): Nome do logradouro associado ao CEP.
- `ibge` (obrigatório): Código IBGE da cidade associada ao CEP.
- `bairro` (obrigatório): Nome do bairro associado ao CEP.
- `cidade` (obrigatório): Nome da cidade associada ao CEP.
- `uf` (obrigatório): Sigla do estado (UF) associado ao CEP.
- `ddd` (obrigatório): Código DDD da cidade associada ao CEP.

## Respostas

A API retorna uma resposta JSON contendo os seguintes campos:

- Em caso de sucesso:
  - `message`: Mensagem de sucesso.
- Em caso de erro:
  - `error`: Descrição do erro.

A API também retorna o código de status HTTP correspondente a cada resposta.

## Exemplos

### Requisição

```http
POST /api/v1/cep/ HTTP/1.1
Content-Type: application/json

{
  "cep": "12345-678",
  "logradouro": "Rua Exemplo",
  "ibge": "1234567",
  "bairro": "Bairro Exemplo",
  "cidade": "Cidade Exemplo",
  "uf": "UF",
  "ddd": 99
}
```