# P0 — Organizador de Anotações

Aplicação em Python que utiliza um Large Language Model (LLM) para transformar anotações textuais livres em informações organizadas, identificando títulos, resumos, pontos importantes e possíveis ações.

Este projeto corresponde ao nível **Básico da entrega P0**, cujo objetivo é demonstrar um primeiro ciclo de desenvolvimento de uma aplicação funcional com integração a um serviço de inteligência artificial.

## 1. Problema

Anotações feitas durante reuniões, aulas, estudos e atividades cotidianas frequentemente são registradas em linguagem natural, sem uma estrutura definida. Isso pode dificultar a identificação posterior das informações principais, dos compromissos e das tarefas mencionadas.

O Note Organizer propõe uma solução simples para esse problema: receber um texto livre e organizá-lo em seções que facilitem sua leitura e compreensão.

## 2. Público-alvo

A aplicação é destinada a pessoas que registram informações em texto livre e desejam organizá-las com menos esforço, especialmente estudantes e pessoas que precisam revisar anotações de reuniões, atividades e tarefas.

## 3. Justificativa para utilização de um LLM

A linguagem utilizada em anotações livres pode variar bastante. Uma mesma informação pode ser expressa de diferentes maneiras, com abreviações, frases incompletas, informações distribuídas pelo texto e diferentes níveis de contextualização.

Uma abordagem baseada exclusivamente em regras fixas exigiria a definição de padrões específicos para reconhecer essas variações.

A utilização de um LLM permite interpretar textos em linguagem natural e identificar relações contextuais entre as informações, produzindo uma organização mais flexível.

O modelo recebe instruções específicas para preservar o significado original, não inventar informações e identificar responsáveis e prazos somente quando estiverem explicitamente presentes no texto.

A utilização do LLM não elimina a necessidade de revisão humana: o resultado deve ser conferido pelo usuário.

## 4. Funcionamento da solução

A aplicação funciona por meio de uma interface de terminal e de uma integração HTTP com a NVIDIA NIM, utilizando uma API compatível com o formato Chat Completions.

O fluxo de execução é composto pelas seguintes etapas:

1. O usuário informa uma anotação pelo terminal.
2. O módulo `organizer.py` valida a entrada e prepara o texto.
3. O módulo `prompts.py` fornece as instruções que orientam a organização.
4. O módulo `llm_client.py` envia as instruções e a anotação ao modelo configurado.
5. A resposta é processada e apresentada no terminal pelo módulo `main.py`.

### Estrutura esperada da resposta

- **Título:** representação breve do conteúdo.
- **Resumo:** síntese das principais informações.
- **Pontos importantes:** assuntos e informações relevantes.
- **Ações identificadas:** tarefas mencionadas, com responsáveis e prazos somente quando explicitamente informados.

### Estrutura do projeto

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
├── RELATORIO_EXECUCAO.md
└── LICENSE
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Interface de entrada e saída pelo terminal. |
| `organizer.py` | Validação da anotação e coordenação da organização. |
| `llm_client.py` | Configuração e comunicação HTTP com o serviço de LLM. |
| `prompts.py` | Definição das instruções enviadas ao modelo. |
| `test_organizer.py` | Testes automatizados da lógica de organização. |

## 5. Limites da solução

O projeto tem escopo intencionalmente limitado ao nível Básico da P0.

A aplicação:

- Não armazena anotações em banco de dados ou arquivos.
- Não possui interface gráfica ou aplicação web.
- Não mantém histórico de anotações.
- Não executa automaticamente as ações identificadas.
- Não verifica a veracidade das informações fornecidas.
- Não garante que todas as informações sejam classificadas corretamente.
- Não garante respostas idênticas para entradas iguais, pois a geração depende do comportamento do modelo.
- Não substitui a revisão do usuário sobre o conteúdo organizado.

O modelo pode interpretar incorretamente informações ambíguas ou produzir classificações inadequadas. Portanto, responsáveis, prazos e ações identificados devem ser conferidos antes de serem utilizados.

Como o texto é enviado a um serviço externo de inferência, não devem ser inseridas credenciais, informações pessoais sensíveis ou dados confidenciais nas anotações.

## 6. Requisitos

- Python 3.10 ou superior.
- Chave de acesso autorizada à NVIDIA NIM.
- Git.

## 7. Instalação

### 7.1. Clonar o repositório

```bash
git clone https://github.com/cauaenzo/P0-application.git
cd P0-application
```

### 7.2. Criar o ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 7.3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 7.4. Instalar o projeto em modo editável

```bash
pip install -e .
```

Essa instalação permite que o Python encontre o pacote localizado em `src/app`.

## 8. Configuração do acesso ao LLM

A aplicação utiliza variáveis de ambiente para separar as credenciais e os parâmetros de acesso do código-fonte.

Crie um arquivo `.env` na raiz do projeto, utilizando `.env.example` como referência:

```env
LLM_API_KEY=nvapi-sua-chave
LLM_BASE_URL=https://integrate.api.nvidia.com/v1
LLM_MODEL=nvidia/nemotron-3.5-super-vl-120b-a12b
```

Substitua `LLM_API_KEY` por uma chave válida e autorizada para utilização do serviço.

As três variáveis são necessárias:

| Variável | Finalidade |
|---|---|
| `LLM_API_KEY` | Credencial de autenticação. |
| `LLM_BASE_URL` | Endereço-base da API. |
| `LLM_MODEL` | Identificador do modelo utilizado. |

**Importante:** o arquivo `.env` contém credenciais e não deve ser versionado. O `.gitignore` impede seu envio acidental ao Git. O arquivo `.env.example` documenta os parâmetros necessários sem expor segredos.

Não compartilhe sua chave de API em repositórios, vídeos, capturas de tela ou documentos públicos.

## 9. Execução

Com o ambiente virtual ativado, as dependências instaladas e as variáveis configuradas, execute:

```bash
python -m app.main
```

A aplicação solicitará uma anotação pelo terminal e apresentará o resultado organizado pelo modelo.

## 10. Exemplo de utilização

**Entrada ilustrativa:**

```text
Tivemos uma reunião sobre o projeto. João vai enviar
a planilha atualizada até terça-feira. Na sexta,
vamos conversar com Marina sobre o cronograma.
Também precisamos revisar os requisitos antes da
próxima reunião.
```

**Exemplo ilustrativo de saída esperada:**

```text
TÍTULO
Reunião sobre o projeto

RESUMO
A reunião abordou o andamento do projeto,
a atualização da planilha, o cronograma
e a revisão dos requisitos.

PONTOS IMPORTANTES
- Atualização da planilha.
- Discussão do cronograma.
- Revisão dos requisitos.

AÇÕES IDENTIFICADAS
- Enviar a planilha atualizada.
  Responsável: João.
  Prazo: terça-feira.

- Conversar sobre o cronograma.
  Responsável: Não informado.
  Prazo: sexta-feira.

- Revisar os requisitos.
  Responsável: Não informado.
  Prazo: Não informado.
```

A saída acima serve para demonstrar o formato pretendido. A resposta efetiva é gerada pelo modelo e pode apresentar variações.

## 11. Testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

### Testes simulados

A suíte inicial utiliza `unittest` e `unittest.mock` para isolar a lógica do organizador da comunicação externa com o modelo.

Os testes verificam:

| Teste | Situação | Resultado esperado |
|---|---|---|
| Organização de anotação | Texto válido com espaços excedentes | Texto normalizado e encaminhado ao cliente de LLM. |
| Rejeição de anotação vazia | Texto composto apenas por espaços | Lançamento de `ValueError`. |

Esses testes não realizam chamadas reais à NVIDIA NIM. A resposta do cliente de LLM é simulada para permitir verificações determinísticas.

### Validação real da integração

Durante o desenvolvimento, foi realizada uma execução manual utilizando a NVIDIA NIM, com credenciais válidas e o modelo configurado.

Essa execução permitiu verificar o fluxo de autenticação, envio da anotação, recebimento da resposta e apresentação do resultado no terminal.

A validação real depende de conexão com a internet, disponibilidade do serviço e credenciais válidas. Ela não faz parte da suíte automatizada.

## 12. Tratamento de falhas

A aplicação contempla algumas situações de erro para evitar que problemas de entrada ou comunicação interrompam o fluxo sem uma mensagem compreensível.

| Situação | Comportamento implementado |
|---|---|
| Anotação vazia | A aplicação informa que o texto não pode estar vazio. |
| Variável de ambiente ausente | O cliente informa qual configuração está faltando. |
| Tempo limite excedido | Retorna uma mensagem de timeout. |
| Falha de conexão | Informa que não foi possível conectar ao serviço. |
| Erro HTTP | Informa o código HTTP retornado. |
| Falha na interpretação da resposta | Informa que a resposta do modelo não pôde ser interpretada. |
| Resposta vazia ou inválida | Informa que o modelo retornou conteúdo inválido. |

A implementação não possui mecanismo de repetição automática de requisições. Falhas temporárias de serviço precisam ser tratadas por uma nova tentativa de execução pelo usuário.

## 13. Limitações conhecidas

A versão atual representa uma implementação inicial e possui as seguintes limitações:

- A aplicação processa uma anotação por execução.
- Não há persistência ou recuperação de resultados anteriores.
- A saída é apresentada como texto, sem validação por um esquema estruturado.
- Não existem testes automatizados abrangentes para todos os erros de comunicação com a API.
- A qualidade da organização depende da clareza da anotação e da interpretação do modelo.
- A disponibilidade da aplicação depende do serviço externo de inferência.

Essas limitações são compatíveis com o escopo do nível Básico e poderão orientar melhorias em etapas posteriores.

## 14. Vídeo de demonstração

**Link:** Pendente de gravação e publicação.

O vídeo será disponibilizado nesta seção após a demonstração da instalação, configuração e execução da aplicação.

## 15. Relatório de execução

O histórico de desenvolvimento, as decisões técnicas, os resultados dos testes, as dificuldades encontradas e o uso de ferramentas de inteligência artificial estão registrados em:

[`RELATORIO_EXECUCAO.md`](RELATORIO_EXECUCAO.md)


## 16. Licença

Consulte o arquivo `LICENSE` para informações sobre a licença do projeto.

## Demonstração

Confira o vídeo de demonstração do Note Organizer:

[Assistir à demonstração no YouTube](https://youtu.be/LAK1vtOupLo)