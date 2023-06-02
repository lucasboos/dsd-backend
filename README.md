# Backend para Aplicação de Sistemas Distribuídos

Este repositório contém o código-fonte do backend desenvolvido pelo grupo para a disciplina de Desenvolvimento de Sistemas Distribuídos do curso de Análise e Desenvolvimento de Sistemas do 5º semestre. Neste projeto, nosso grupo é responsável pela implementação do backend de uma aplicação distribuída.

## Alunos

Este repositório do GitHub é dedicado ao trabalho em grupo realizado pelos seguintes alunos:

- Arthur M.
- Lucas B.
- Pablo L.
- Paolo B.
- Vinicius N.

## Objetivo

O objetivo deste projeto é desenvolver o backend de uma aplicação de Sistemas Distribuídos, que será responsável por gerenciar a lógica de negócios e a comunicação com outros componentes distribuídos.

## Tecnologias Utilizadas

- Linguagem de programação: Python
- Framework: Flask
- Autenticação e autorização: JWT (JSON Web Tokens)
- Comunicação entre componentes: RESTful API
- Controle de versão: Git

## Estrutura do Repositório

- `apps/`: Diretório principal do código-fonte do backend.
- `apps/<>/models.py`: Contém as definições dos modelos de dados utilizados na aplicação.
- `apps/<>/controllers.py`: Implementa a lógica de negócios da aplicação, incluindo as operações de CRUD (Create, Read, Update, Delete).
- `apps/<>/web.py`: Define as rotas da API RESTful para acesso aos recursos do backend.
- `apps/utils.py`: Contém funções utilitárias e helpers.
- `apps/factory.py`: Cria a aplicação Flask, configura o suporte a CORS e JWT, e registra a blueprint relacionado às rotas e lógica dos usuários.
- `run.py`: Arquivo de configuração da aplicação, contendo variáveis de ambiente, configurações específicas e inicialização.
- `sample_ini`: Configurações de ambiente usadas para fornecer as informações de conexão do banco de dados em diferentes ambientes.
- `requirements.txt`: Lista de dependências do projeto para fácil instalação.

## Contribuição

Cada aluno do grupo é responsável por contribuir com o desenvolvimento do projeto. Trabalhando em diferentes aspectos, como implementação de funcionalidades, correção de bugs, entre outros. É incentivada a colaboração, revisão de código e discussões construtivas entre os membros do grupo.

## Contato

Em caso de dúvidas ou informações adicionais, entre em contato com qualquer um dos membros do grupo mencionados acima.

## Instalação

### Criar o ambiente virtual
```
cd backend
python -m venv venv
```

### Ativar o ambiente virtual

*Windows*
```
venv\Scripts\activate
```
*Linux / Mac OS*
```
source venv/bin/activate
```

### Instalação dos pacotes
```
pip install -r requirements.txt
```

### Iniciar a aplicação

Obs. tenha certeza que o ambiente virtual esteja habilitado.

```
python run.py
```
