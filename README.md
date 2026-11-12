<div align="center">

# The-Creators

**Ideias de viagem, organizadas para ir mais longe.**

Uma aplicação web acadêmica em desenvolvimento para explorar a América do Sul e organizar registros de viagem.

</div>

---

## Visão geral

The-Creators é um projeto colaborativo desenvolvido por quatro estudantes. A proposta do **Passaporte Sul-Americano** é permitir que cada usuário consulte informações sobre os 12 países da América do Sul e a Guiana Francesa, registre suas viagens e veja as localidades visitadas no mapa.

## Objetivos

- Praticar programação orientada a objetos em Python.
- Implementar rotas Flask para consultar localidades, gerenciar contas e registrar viagens.
- Usar MariaDB para armazenar países, usuários e visitas.
- Conectar a interface em HTML, CSS e JavaScript às rotas do back-end com a Fetch API.

## Tecnologias

| Área | Tecnologia ou escopo |
| --- | --- |
| Backend | Python e Flask |
| Programação | Orientação a objetos (POO) e DAOs |
| Frontend | HTML, CSS e JavaScript |
| Integração | Fetch API para conectar a interface às rotas Flask |
| Banco de dados | MariaDB com PyMySQL |

## Funcionalidades e estado atual

### Presente no repositório

- Rotas Flask para consultar localidades, cadastrar usuários, fazer login e registrar e consultar viagens.
- Classes Python, DAOs para acesso ao banco e testes do fluxo do backend.
- Arquivos iniciais do frontend e um script SQL com as tabelas e os dados das 13 localidades.

### Proposto, ainda em desenvolvimento

- Exibir um mapa interativo com informações sobre cada país ou território.
- Conectar os formulários da interface às rotas Flask com a Fetch API.
- Mostrar uma estrela nas localidades visitadas e recuperar as marcações salvas ao recarregar a página.

## Arquitetura

```text
The-Creators/
├── backend/
│   ├── Classes/
│   │   ├── app.py
│   │   ├── conexao.py
│   │   ├── pais.py
│   │   ├── rotas_paises.py
│   │   ├── rotas_usuarios.py
│   │   ├── rotas_visitas.py
│   │   ├── usuario.py
│   │   └── visita.py
│   ├── dao/
│   │   ├── pais_dao.py
│   │   ├── usuario_dao.py
│   │   └── visita_dao.py
│   ├── config.py
│   └── requirements.txt
├── database/
│   └── passaporte_sulamericano.sql
├── frontend/
│   ├── css/
│   ├── js/
│   └── index.html
├── tests/
│   └── test_fluxo.py
├── .env.example
├── .gitignore
└── README.md
```

A aplicação Flask, a conexão, as classes e as rotas ficam em `backend/Classes/`. Os DAOs em `backend/dao/` executam as consultas e gravações no MariaDB.

## Configuração e execução

### Pré-requisitos

- Git para clonar o repositório.
- Python 3 instalado.
- Um servidor MariaDB local, como o do XAMPP.

### Preparar o ambiente

Clone o repositório e entre na pasta do projeto.

```bash
git clone https://github.com/damascenoluanfonseca-jpg/The-Creators.git
cd The-Creators
```

Crie um ambiente virtual e instale as dependências de `backend/requirements.txt`.

**Linux ou macOS**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r backend/requirements.txt
```

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
```

### Configurações locais

Se estiver usando o XAMPP, inicie o serviço **MySQL** no painel. Na primeira configuração, crie e selecione o banco `passaporte_sulamericano` no phpMyAdmin e importe `database/passaporte_sulamericano.sql`.

Use `.env.example` e `backend/Classes/conexao.py` como referência. Ajuste `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` e `DB_NAME` no terminal conforme a configuração do seu banco.

### Iniciar o backend

Na raiz do repositório, gere a chave de sessão e inicie o Flask no mesmo terminal.

**Linux ou macOS**

```bash
export FLASK_SECRET_KEY="$(.venv/bin/python -c 'from secrets import token_hex; print(token_hex(32))')"
.venv/bin/python -m flask --app backend.Classes.app run
```

**Windows PowerShell**

```powershell
$env:FLASK_SECRET_KEY = & .\.venv\Scripts\python.exe -c "from secrets import token_hex; print(token_hex(32))"
.\.venv\Scripts\python.exe -m flask --app backend.Classes.app run
```

Abra a [rota de status](http://127.0.0.1:5000/api/status) para conferir se o Flask respondeu. Em seguida, abra a [rota de países](http://127.0.0.1:5000/api/paises). Com os dados iniciais importados, a rota deve retornar as 13 localidades em JSON.

### Rodar os testes

Com o banco de desenvolvimento configurado e ligado, execute na pasta principal.

- Windows PowerShell — `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`
- Linux ou macOS — `.venv/bin/python -m unittest discover -s tests -v`

## Fluxo de desenvolvimento

1. Mantenha `main` como branch estável.
2. Crie uma branch para cada tarefa, como `feat/mapa` ou `docs/readme`.
3. Faça commits pequenos com mensagens claras, como `feat: adiciona cadastro de visitas`.
4. Abra um Pull Request para revisão antes de integrar as alterações.
5. Atualize a documentação quando a configuração, a estrutura ou o comportamento do sistema mudar.
6. Guarde arquivos `.env`, senhas e chaves fora dos commits.

## Equipe

| Integrante | Nome |
| --- | --- |
| 1 | Luan Fonseca |
| 2 | Victor Moreira |
| 3 | Lorenzo Cruz |
| 4 | Pedro Brandão |

## Status

**Em desenvolvimento.** A integração do mapa e dos formulários com as rotas Flask faz parte da etapa final.
