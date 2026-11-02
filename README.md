# P0 — Organizador de Anotações

Aplicação em Python que utiliza um Large Language Model (LLM) para transformar anotações textuais livres em informações organizadas, identificando títulos, resumos, pontos importantes e possíveis ações.

Este projeto faz parte da primeira entrega (P0 — Básico) de uma jornada de desenvolvimento com Inteligência Artificial, com foco na integração direta com APIs de LLM, organização de código Python e boas práticas de desenvolvimento reproduzível.

## Objetivo

Desenvolver uma aplicação simples que receba anotações em linguagem natural pelo terminal e utilize um modelo de linguagem para organizar seu conteúdo.

A aplicação busca identificar:

- **Título:** representação breve do conteúdo.
- **Resumo:** síntese das principais informações.
- **Pontos importantes:** assuntos e informações relevantes.
- **Ações identificadas:** tarefas mencionadas, incluindo responsáveis e prazos somente quando explicitamente informados.

O sistema deve preservar o significado original da anotação e evitar inventar informações ausentes.

## Tecnologias utilizadas

- **Python:** linguagem principal.
- **NVIDIA NIM:** provedor de inferência do modelo de linguagem.
- **Requests:** comunicação HTTP com a API.
- **python-dotenv:** carregamento de variáveis de ambiente.
- **unittest:** testes automatizados.
- **Git e GitHub:** controle de versão.

A integração com o modelo utiliza uma API compatível com o formato Chat Completions, sem dependência de frameworks de agentes ou orquestração.

## Estrutura do projeto

```text
P0-application/
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── organizer.py
│       ├── llm_client.py
│       └── prompts.py
├── tests/
│   └── test_organizer.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Interface de entrada e saída pelo terminal. |
| `organizer.py` | Coordenação do processo de organização. |
| `llm_client.py` | Comunicação com a API do modelo. |
| `prompts.py` | Definição das instruções enviadas ao modelo. |
| `test_organizer.py` | Testes automatizados da lógica de organização. |

## Requisitos

- Python 3.10 ou superior.
- Chave de API da NVIDIA NIM.
- Git.

## Configuração do ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/cauaenzo/P0-application.git
cd P0-application
```

### 2. Criar o ambiente virtual

Windows:

```powershell
python -m venv venv
venv\Scripts\Activate
```

Linux e macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Instalar o projeto em modo editável

```bash
pip install -e .
```

Essa instalação permite que o Python encontre o pacote localizado em `src/app`.

### 5. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando `.env.example` como referência:

```env
LLM_API_KEY=nvapi-sua-chave
LLM_BASE_URL=https://integrate.api.nvidia.com/v1
LLM_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
```

Substitua o valor de `LLM_API_KEY` pela sua chave de API.

**Importante:** o arquivo `.env` contém credenciais e não deve ser enviado ao Git. Utilize `.env.example` para documentar as variáveis necessárias sem expor informações sensíveis.

## Executando a aplicação

Com o ambiente virtual ativado e as variáveis configuradas:

```bash
python -m app.main
```

A aplicação solicitará uma anotação pelo terminal e apresentará o resultado organizado pelo modelo.

## Executando os testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

Os testes unitários utilizam mocks para verificar a lógica de organização sem depender de chamadas reais à API.

## Escopo atual

Esta versão corresponde ao nível Básico da entrega P0.

O escopo inicial contempla:

- Recebimento de texto pelo terminal.
- Integração programática com um LLM.
- Organização de anotações por meio de instruções específicas.
- Configuração externa de credenciais.
- Declaração de dependências.
- Testes unitários iniciais.

Funcionalidades adicionais e melhorias estruturais poderão ser incorporadas incrementalmente nas próximas etapas.

## Licença

Consulte o arquivo `LICENSE` para informações sobre a licença do projeto.