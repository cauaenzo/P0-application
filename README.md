# P0 — Note Organizer

Aplicação de linha de comando desenvolvida em Python para organizar anotações textuais utilizando um modelo de linguagem (LLM).

O projeto recebe uma anotação escrita pelo usuário e utiliza a NVIDIA NIM para gerar uma versão estruturada, contendo título, resumo, pontos importantes e ações identificadas.

O desenvolvimento está organizado em três níveis de evolução: Básico, Intermediário e Avançado.

## 1. Objetivo

O objetivo do projeto é desenvolver uma aplicação capaz de transformar anotações livres em informações mais organizadas, facilitando sua leitura e compreensão.

A aplicação utiliza um modelo de linguagem para interpretar o conteúdo fornecido e produzir uma resposta estruturada, contendo título, resumo, pontos importantes e ações identificadas, buscando preservar o significado original da anotação.

O público-alvo inclui estudantes e pessoas que trabalham com anotações textuais e desejam transformar registros livres em informações mais estruturadas, facilitando a identificação de assuntos importantes e atividades a serem realizadas.

A utilização de um modelo de linguagem permite interpretar anotações escritas livremente, mesmo quando apresentam estruturas, vocabulários e formas de expressão diferentes. Uma abordagem baseada exclusivamente em regras fixas exigiria definir previamente diversos padrões de entrada, tornando a solução menos flexível diante de textos variados.

## 2. Funcionalidades

### P0 — Básico

- Recebimento de anotações pelo terminal.
- Integração com a NVIDIA NIM por meio de requisições HTTP.
- Organização do conteúdo em título, resumo, pontos importantes e ações.
- Configuração do modelo e das credenciais por variáveis de ambiente.
- Separação inicial das responsabilidades em módulos.
- Testes unitários da funcionalidade principal.

### P0 — Intermediário

- Validação das configurações necessárias para acessar o serviço de LLM.
- Verificação da presença da credencial, endereço do serviço e identificação do modelo.
- Validação do formato do endereço configurado.
- Preparação da requisição em uma função específica.
- Separação entre envio da requisição e interpretação da resposta.
- Tratamento de falhas de conexão, timeout e erros HTTP.
- Identificação de respostas vazias, inválidas ou inesperadas.
- Exibição de mensagens de erro compreensíveis no terminal.
- Ampliação da cobertura de testes automatizados, utilizando simulação das respostas do serviço externo.

### P0 — Avançado

Ainda não implementado.

## 3. Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Requests:** realização de requisições HTTP.
- **Python-dotenv:** carregamento de variáveis de ambiente a partir de arquivos `.env`.
- **Unittest:** execução dos testes automatizados.
- **Unittest.mock:** simulação de componentes externos durante os testes.
- **NVIDIA NIM:** serviço de inferência utilizado para gerar as respostas do modelo.

## 4. Estrutura do projeto

```text
P0-application/
│
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── llm_client.py
│       ├── organizer.py
│       └── prompts.py
│
├── tests/
│   ├── test_config.py
│   ├── test_llm_client.py
│   ├── test_main.py
│   └── test_organizer.py
│
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
├── RELATORIO_EXECUCAO.md
└── LICENSE
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Captura a entrada do usuário, valida o conteúdo e apresenta o resultado ou mensagens de erro. |
| `config.py` | Carrega e valida as configurações necessárias para acessar o serviço de LLM. |
| `llm_client.py` | Prepara e envia requisições, trata falhas de comunicação e interpreta as respostas do modelo. |
| `organizer.py` | Coordena o processo de organização da anotação. |
| `prompts.py` | Armazena as instruções utilizadas para orientar o modelo de linguagem. |

A pasta `tests/` contém os testes automatizados organizados conforme as responsabilidades dos módulos da aplicação.

## 5. Requisitos

Para executar o projeto, são necessários:

- Python 3.10 ou superior.
- Git.
- Acesso à internet para comunicação com a NVIDIA NIM.
- Uma credencial válida para acessar o serviço.

## 6. Instalação

Clone o repositório:

```bash
git clone https://github.com/cauaenzo/P0-application.git
```

Entre na pasta do projeto:

```bash
cd P0-application
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Windows — PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows — Git Bash:**

```bash
source .venv/Scripts/activate
```

**Linux:**

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale o projeto em modo editável:

```bash
pip install -e .
```

## 7. Configuração

Crie um arquivo chamado `.env` na raiz do projeto, utilizando o `.env.example` como referência.

Configure as seguintes variáveis:

```env
LLM_API_KEY=nvapi-sua-chave
LLM_BASE_URL=https://integrate.api.nvidia.com/v1
LLM_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
```

### Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `LLM_API_KEY` | Credencial de autenticação para acessar o serviço. |
| `LLM_BASE_URL` | Endereço-base da API utilizada. |
| `LLM_MODEL` | Identificação do modelo de linguagem solicitado. |

A credencial deve ser obtida por meio de um provedor autorizado e mantida exclusivamente no arquivo `.env`.

O arquivo `.env` está incluído no `.gitignore` para evitar que credenciais sejam enviadas acidentalmente ao repositório.

**Importante:** nunca compartilhe sua chave de API ou publique credenciais no código-fonte.

## 8. Execução

Com o ambiente virtual ativado e as configurações preenchidas, execute:

```bash
python -m app.main
```

A aplicação solicitará uma anotação pelo terminal.

### Exemplo de entrada

```text
Digite sua anotação:

> Amanhã preciso revisar o conteúdo de Python,
> finalizar o exercício de programação e
> conversar com o professor sobre o trabalho.
```

### Exemplo de saída

```text
=== Anotação organizada ===

Título:
Organização das atividades acadêmicas

Resumo:
Planejamento de atividades relacionadas ao
estudo de Python e ao desenvolvimento de um trabalho.

Pontos importantes:
- Revisar o conteúdo de Python.
- Finalizar o exercício de programação.
- Conversar com o professor sobre o trabalho.

Ações:
- Revisar Python.
- Finalizar o exercício.
- Conversar com o professor.
```

A resposta apresentada é ilustrativa. O conteúdo efetivamente produzido depende da interpretação realizada pelo modelo de linguagem.

## 9. Tratamento de erros

A versão Intermediária amplia o tratamento de falhas para evitar que problemas previsíveis interrompam a aplicação com mensagens técnicas pouco compreensíveis.

Entre os cenários contemplados estão:

| Situação | Comportamento esperado |
|---|---|
| Anotação vazia | Rejeição da entrada antes da chamada ao serviço. |
| Credencial ausente | Exibição de mensagem informando a necessidade de configurar `LLM_API_KEY`. |
| Endereço ausente ou inválido | Exibição de mensagem indicando problema em `LLM_BASE_URL`. |
| Modelo não configurado | Exibição de mensagem indicando a necessidade de configurar `LLM_MODEL`. |
| Credencial inválida | Identificação de erro de autenticação HTTP 401. |
| Falta de autorização | Identificação de erro HTTP 403. |
| Modelo ou endpoint não encontrado | Identificação de erro HTTP 404. |
| Limite de requisições atingido | Identificação de erro HTTP 429. |
| Serviço indisponível | Tratamento de erros HTTP 5xx. |
| Falha de conexão | Exibição de mensagem informando a impossibilidade de conexão. |
| Timeout | Exibição de mensagem informando que o serviço demorou demais para responder. |
| Resposta vazia ou inválida | Rejeição do conteúdo retornado pelo modelo. |
| Estrutura inesperada | Exibição de mensagem indicando que não foi possível interpretar a resposta. |

Os erros esperados são tratados e apresentados ao usuário sem a necessidade de exibir um traceback completo no terminal.

## 10. Testes automatizados

O projeto utiliza `unittest` para verificar o comportamento dos módulos e `unittest.mock` para simular componentes externos, especialmente as requisições HTTP.

Para executar a suíte de testes:

```bash
python -m unittest discover -s tests -v
```

### Cobertura atual

Os 22 testes automatizados estão distribuídos entre quatro módulos:

| Arquivo | Quantidade de testes |
|---|---:|
| `test_config.py` | 4 |
| `test_llm_client.py` | 12 |
| `test_main.py` | 4 |
| `test_organizer.py` | 2 |
| **Total** | **22** |

Os testes verificam, entre outros aspectos:

- Carregamento e validação das configurações.
- Preparação dos dados da requisição.
- Tratamento de erros HTTP.
- Falhas de conexão e timeout.
- Interpretação de respostas válidas e inválidas.
- Rejeição de anotações vazias.
- Comportamento da interface de terminal diante de erros.

**Resultado da última execução registrada:**

```text
Ran 22 tests

OK
```

Os testes automatizados utilizam simulações e não dependem de chamadas reais à NVIDIA NIM. Portanto, a aprovação da suíte verifica a lógica implementada, mas não garante, isoladamente, a disponibilidade do serviço externo ou a validade de uma credencial real.

É importante distinguir os dois tipos de validação realizados:

- **Validação real:** a versão Básica foi executada utilizando a integração com a NVIDIA NIM.
- **Testes simulados:** os 22 testes automatizados da versão Intermediária utilizam mocks para simular respostas e falhas do serviço externo.

Assim, os testes automatizados verificam o comportamento da aplicação em diferentes cenários, mas não representam 22 chamadas reais à API.

## 11. Arquitetura e decisões técnicas

A aplicação foi organizada para separar as responsabilidades envolvidas no processamento de uma anotação.

O fluxo principal pode ser representado da seguinte maneira:

```text
Entrada do usuário
       |
       v
    main.py
       |
       v
  organizer.py
       |
       v
   prompts.py
       |
       v
  llm_client.py
       |
       +---- config.py
       |
       v
   NVIDIA NIM
       |
       v
 Interpretação da resposta
       |
       v
 Apresentação no terminal
```

A integração com o serviço externo é realizada diretamente por meio de requisições HTTP utilizando `requests`, sem a adoção de frameworks de agentes ou abstrações adicionais de LLM.

Essa decisão mantém o fluxo de comunicação explícito e permite controlar diretamente a preparação da requisição, o envio dos dados, o tratamento dos erros e a interpretação da resposta.

O módulo `config.py` fornece as configurações utilizadas pelo `llm_client.py`, mantendo a responsabilidade de carregamento e validação separada da comunicação com o serviço externo.

## 12. Limitações conhecidas

Apesar da evolução da estrutura e do tratamento de erros, algumas limitações permanecem:

- A qualidade da organização depende da interpretação realizada pelo modelo de linguagem.
- O modelo pode interpretar expressões ambíguas como possíveis ações.
- A aplicação depende da disponibilidade do serviço externo.
- Não existe uma etapa independente de validação semântica para verificar se todas as informações produzidas correspondem fielmente à anotação original.
- A interface permanece restrita ao terminal.

Essas limitações podem ser abordadas em etapas futuras do desenvolvimento.

## 13. Demonstração

A demonstração em vídeo da versão Intermediária será disponibilizada após a gravação e validação da execução correspondente.

A demonstração da versão Básica está disponível em:

[Assistir à demonstração do P0 Básico](https://youtu.be/LAK1vtOupLo)

## 14. Relatório de execução

O arquivo `RELATORIO_EXECUCAO.md` apresenta o histórico de desenvolvimento, as decisões técnicas, os testes realizados, as dificuldades encontradas e a utilização de ferramentas de inteligência artificial durante o projeto.

## 15. Licença

Este projeto está disponibilizado sob a licença definida no arquivo `LICENSE`.