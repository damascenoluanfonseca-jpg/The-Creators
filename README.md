<div align="center">

# The-Creators

**Explore o mundo. Organize suas próximas ideias de viagem.**

Uma plataforma acadêmica em desenvolvimento para descoberta de destinos internacionais e organização de informações de viagem.

</div>

---

## Sobre o projeto

The-Creators é um projeto colaborativo desenvolvido por quatro estudantes. A proposta é criar uma aplicação web de viagens com frontend em HTML, CSS e JavaScript, backend em Python com Flask e integração por meio da Fetch API.

O projeto está em fase inicial. O escopo funcional e o banco de dados ainda estão sendo definidos; por isso, este README distingue a proposta do que já está implementado.

## Tecnologias

| Camada | Tecnologia |
| --- | --- |
| Backend e API | Python, Flask e programação orientada a objetos (OOP) |
| Interface | HTML, CSS e JavaScript |
| Comunicação | Fetch API — prevista para a integração entre frontend e backend |
| Persistência | Banco de dados relacional — mecanismo a definir pela equipe |

## Objetivos

- Desenvolver uma aplicação web relacionada a viagens internacionais.
- Criar uma base para explorar destinos e organizar informações de viagem.
- Integrar uma interface web a rotas Flask usando JavaScript e Fetch.
- Praticar modelagem, orientação a objetos e colaboração em equipe.

## Funcionalidades

**Proposta do projeto:** descoberta de destinos internacionais e organização de informações de viagem.

Os fluxos e recursos finais ainda não foram definidos. Não considere funcionalidades da proposta como implementadas até que estejam confirmadas no código e pela equipe.

## Arquitetura atual

A estrutura abaixo reflete os diretórios presentes no repositório. É um scaffold inicial e pode evoluir conforme o sistema for implementado.

```text
The-Creators/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── dao/
│   ├── models/
│   └── routes/
├── database/
│   └── seed.sql
├── docs/
│   ├── README.md
│   └── architecture.md
├── frontend/
│   ├── css/
│   ├── index.html
│   └── js/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

As pastas `dao/`, `models/` e `routes/` são pontos de organização do backend; suas implementações podem estar em andamento. O mecanismo de banco de dados não foi especificado. Consulte a equipe antes de definir configurações ou scripts dependentes de um banco específico.

## Configuração e execução

Os comandos abaixo pressupõem Python instalado e execução a partir da raiz do repositório.

1. Clone o projeto e entre na pasta:

   ```bash
   git clone https://github.com/damascenoluanfonseca-jpg/The-Creators.git
   cd The-Creators
   ```

2. Crie e ative um ambiente virtual:

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

3. Instale as dependências declaradas no projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Quando a aplicação exigir configurações locais, use `.env.example` como referência e crie um `.env`. Preencha apenas valores apropriados ao seu ambiente. **Nunca** inclua credenciais reais em commits.

5. Inicie o backend:

   ```bash
   python backend/app.py
   ```

A execução disponível é um ponto de partida para desenvolvimento; rotas, persistência e integração completa devem ser confirmadas conforme a aplicação evoluir. O banco de dados e sua configuração ainda dependem de decisão da equipe.

## Fluxo de desenvolvimento

- Mantenha `main` como branch estável.
- Crie branches curtas para tarefas específicas, por exemplo `feat/destination-list` ou `docs/setup`.
- Abra um Pull Request para revisão antes de integrar mudanças.
- Prefira commits pequenos e objetivos, usando mensagens claras, como `feat: add destination model` ou `docs: clarify setup`.
- Atualize a documentação quando uma alteração modificar a configuração, a estrutura ou o comportamento do sistema.
- Não envie arquivos `.env`, senhas, tokens ou outras credenciais.

## Equipe

Projeto desenvolvido por quatro estudantes. Os nomes e usuários do GitHub ainda não foram informados; esta seção será atualizada quando a equipe confirmar os dados.

| Integrante | Nome / usuário |
| --- | --- |
| 1 | A confirmar |
| 2 | A confirmar |
| 3 | A confirmar |
| 4 | A confirmar |

## Status

**Em desenvolvimento.** A proposta e a estrutura inicial estão documentadas. Escopo final, banco de dados e funcionalidades ainda precisam ser acordados e implementados pela equipe.

---

<sub>Uma base acadêmica para explorar ideias de viagem — construída passo a passo.</sub>
