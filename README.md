<div align="center">

# The-Creators

**Ideias de viagem, organizadas para ir mais longe.**

Uma aplicação web acadêmica em desenvolvimento, dedicada à descoberta de destinos internacionais e à organização de informações de viagem.

</div>

---

## Visão geral

The-Creators é um projeto colaborativo desenvolvido por quatro estudantes. A proposta é construir uma experiência web para explorar destinos internacionais e reunir informações relacionadas a viagens.

O repositório contém uma estrutura inicial para backend Flask, frontend e scripts de banco de dados. A aplicação ainda está em desenvolvimento: os fluxos finais, o banco de dados e as funcionalidades completas precisam ser definidos pela equipe.

## Objetivos

- Desenvolver uma aplicação web relacionada a viagens internacionais.
- Praticar programação orientada a objetos com Python e Flask.
- Conectar uma interface em HTML, CSS e JavaScript a rotas do backend.
- Usar Fetch API para comunicação entre frontend e backend, conforme a integração for implementada.
- Definir e implementar a persistência de dados após a escolha do banco pela equipe.

## Tecnologias

| Área | Tecnologia ou escopo |
| --- | --- |
| Backend | Python e Flask |
| Programação | Orientação a objetos (OOP) |
| Frontend | HTML, CSS e JavaScript |
| Integração | Fetch API — prevista no escopo do projeto |
| Banco de dados | Relacional — mecanismo a definir pela equipe |

> A tabela descreve a base técnica e os requisitos do projeto; não indica que todas as integrações já estejam concluídas.

## Funcionalidades e estado atual

### Presente no repositório

- Scaffold de uma aplicação Flask com uma rota inicial.
- Estrutura de pastas para rotas, modelos e acesso a dados.
- Arquivos iniciais de frontend e um script SQL de seed.

### Proposto, ainda em desenvolvimento

- Explorar destinos internacionais.
- Organizar informações relacionadas a viagens.
- Integrar o frontend ao backend usando Fetch API.
- Conectar o sistema a um banco de dados relacional, após a definição do mecanismo.

Os fluxos e recursos finais ainda precisam ser acordados. Os itens propostos não devem ser considerados funcionalidades concluídas.

## Arquitetura

Estrutura observada no repositório:

```text
The-Creators/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── dao/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── routes/
│   │   └── __init__.py
│   ├��─ __init__.py
│   ├── app.py
│   └── config.py
├── database/
│   └── seed.sql
├── docs/
│   ├── README.md
│   └── architecture.md
├── frontend/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── app.js
│   └── index.html
├── .env.example
├── .gitignore
└── requirements.txt
```

As pastas `dao/`, `models/` e `routes/` fazem parte da estrutura atual; a presença delas não significa que essas camadas estejam concluídas. O mecanismo de banco de dados ainda precisa ser confirmado pela equipe.

## Configuração e execução

### Pré-requisitos

- Python instalado.
- A partir da raiz do repositório, consulte `requirements.txt` para as dependências do projeto.
- O mecanismo e a configuração do banco de dados ainda serão definidos pela equipe.

### Preparar o ambiente

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/damascenoluanfonseca-jpg/The-Creators.git
cd The-Creators
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências listadas no arquivo do projeto:

```bash
pip install -r requirements.txt
```

### Configurações locais

Use `.env.example` como referência quando forem necessárias configurações locais. Não adicione senhas, tokens, chaves ou credenciais reais ao repositório.

### Iniciar o backend

A partir da raiz do repositório:

```bash
python backend/app.py
```

A execução corresponde ao scaffold disponível; a integração completa com frontend e banco de dados depende das implementações e decisões da equipe.

## Fluxo de desenvolvimento

1. Mantenha `main` como branch estável.
2. Crie uma branch curta para cada tarefa, por exemplo, `feat/destination-list` ou `docs/setup`.
3. Abra um Pull Request para revisão antes de integrar as alterações.
4. Faça commits pequenos, com mensagens claras e consistentes, como `feat: add destination model` ou `docs: clarify setup`.
5. Atualize a documentação quando uma mudança afetar configuração, estrutura ou comportamento.
6. Nunca inclua arquivos `.env` nem credenciais em commits.

## Equipe

Projeto desenvolvido por quatro estudantes. Os nomes e usuários do GitHub ainda não foram informados.

| Integrante | Nome / usuário do GitHub |
| --- | --- |
| 1 | A confirmar |
| 2 | A confirmar |
| 3 | A confirmar |
| 4 | A confirmar |

## Status

**Em desenvolvimento.** O repositório contém a estrutura inicial do projeto. O escopo funcional, a escolha do banco de dados e a integração entre as camadas ainda precisam ser finalizados pela equipe.
