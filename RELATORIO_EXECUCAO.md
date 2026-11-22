# Relatório de Execução — P0: Note Organizer

## 1. Evolução por nível

### P0 — Básico

**Status: Concluído.**

Foi desenvolvida uma aplicação Python que recebe anotações pelo terminal e utiliza um modelo de linguagem para organizá-las em título, resumo, pontos importantes e ações.

A versão inicial implementou a integração com a NVIDIA NIM, configuração por variáveis de ambiente, organização modular do código e testes da funcionalidade principal.

### P0 — Intermediário

**Status: Implementação concluída.**

A versão Intermediária ampliou a estrutura inicial com:

- Módulo específico para carregamento e validação das configurações.
- Validação da credencial, endereço da API e identificação do modelo.
- Separação da preparação da requisição e interpretação da resposta.
- Tratamento de erros HTTP, conexão e timeout.
- Identificação de respostas vazias ou inesperadas.
- Ampliação da suíte de testes de 2 para 22 testes automatizados.

### P0 — Avançado

**Status: Não iniciado.**

Não foram implementadas funcionalidades correspondentes a este nível.

## 2. Decisões principais

### 2.1. Integração direta com a NVIDIA NIM

- **Decisão:** utilizar `requests` para realizar requisições HTTP.
- **Alternativa:** utilizar frameworks de agentes ou bibliotecas de abstração de LLM.
- **Justificativa:** manter o fluxo de comunicação explícito e evitar dependências desnecessárias.

### 2.2. Interface de terminal

- **Decisão:** utilizar o terminal como interface de entrada e saída.
- **Alternativa:** desenvolver uma interface gráfica ou aplicação web.
- **Justificativa:** concentrar o desenvolvimento na integração com o modelo e na organização das anotações.

### 2.3. Configuração por variáveis de ambiente

- **Decisão:** utilizar `.env` para armazenar credenciais e parâmetros de acesso.
- **Alternativa:** definir configurações diretamente no código.
- **Justificativa:** separar configurações do código-fonte e reduzir o risco de exposição de credenciais.

### 2.4. Separação de responsabilidades

- **Decisão:** distribuir as funcionalidades entre módulos específicos.
- **Alternativa:** concentrar a implementação em um único arquivo.
- **Justificativa:** facilitar manutenção, testes e identificação de falhas.

### 2.5. Testes automatizados com simulação

- **Decisão:** utilizar `unittest` e `unittest.mock` para verificar o comportamento da aplicação.
- **Alternativa:** depender exclusivamente de chamadas reais à API.
- **Justificativa:** permitir testes determinísticos sem depender de conexão, disponibilidade do serviço ou credenciais válidas.

## 3. Testes e resultados

Os testes automatizados utilizam simulações para verificar o comportamento da aplicação sem realizar chamadas reais à NVIDIA NIM.

A tabela apresenta os principais cenários verificados, como síntese dos 22 testes automatizados implementados.

| Teste | Entrada ou situação | Resultado esperado | Resultado obtido |
| :---- | :------------------ | :----------------- | :--------------- |
| Organização de anotação | Texto válido | Encaminhamento ao cliente de LLM | Aprovado |
| Entrada vazia | Texto composto por espaços | Rejeição da entrada | Aprovado |
| Configuração válida | Variáveis preenchidas corretamente | Carregamento da configuração | Aprovado |
| Credencial ausente | `LLM_API_KEY` não configurada | Erro de configuração | Aprovado |
| Modelo ausente | `LLM_MODEL` não configurada | Erro de configuração | Aprovado |
| Endereço inválido | URL em formato incorreto | Erro de configuração | Aprovado |
| Credencial inválida | Resposta HTTP 401 | Mensagem de erro de autenticação | Aprovado |
| Falta de autorização | Resposta HTTP 403 | Mensagem de erro de autorização | Aprovado |
| Modelo ou endpoint não encontrado | Resposta HTTP 404 | Mensagem de erro correspondente | Aprovado |
| Limite de requisições | Resposta HTTP 429 | Mensagem de limite atingido | Aprovado |
| Indisponibilidade do serviço | Resposta HTTP 5xx | Mensagem de indisponibilidade | Aprovado |
| Falha de conexão | Exceção de conexão simulada | Mensagem de falha de conexão | Aprovado |
| Timeout | Tempo limite simulado | Mensagem de timeout | Aprovado |
| Resposta inválida | JSON ou estrutura inesperada | Rejeição da resposta | Aprovado |
| Resposta vazia | Conteúdo sem texto | Rejeição da resposta | Aprovado |

**Resultado da última execução automatizada:**

```text
Ran 22 tests in 0.020s

OK
```

Os 22 testes foram aprovados. Os cenários de comunicação e falha do serviço externo foram verificados por simulação.

Na versão Básica, também foi realizada uma validação manual da integração real com a NVIDIA NIM, utilizando credenciais e modelo configurados. Essa validação confirmou o fluxo de comunicação naquela etapa, mas não representa a execução real de todos os cenários de falha da versão Intermediária.

## 4. Falhas e limitações

Durante a validação manual da versão Básica, uma expressão genérica como "vamos lá" foi interpretada pelo modelo como uma possível ação, embora não representasse necessariamente uma tarefa concreta.

O comportamento foi identificado pela análise da resposta produzida durante a execução. Como tentativa de mitigação, as instruções do prompt foram ajustadas para orientar o modelo a preservar o significado original da anotação e evitar a criação de informações não mencionadas.

Apesar desse ajuste, a interpretação ainda pode apresentar inconsistências. A versão Intermediária aprimorou o tratamento de falhas técnicas, mas não implementou uma etapa independente de validação semântica das respostas. Por isso, a limitação permanece.

## 5. Uso de IA no desenvolvimento

### ChatGPT

- **Ferramenta utilizada:** ChatGPT.
- **Tarefas delegadas:** apoio ao planejamento, análise de decisões técnicas, estruturação do código, revisão de testes e documentação.
- **Resultado aproveitado:** orientações para separação de responsabilidades, validação de configurações, tratamento de exceções e ampliação da cobertura de testes.
- **Correções realizadas:** as sugestões foram avaliadas, adaptadas e revisadas conforme a implementação e os requisitos do projeto.
- **Verificação:** execução local da aplicação e dos testes automatizados.

### NVIDIA NIM

Utilizada como serviço externo de inferência para processar as anotações. Sua utilização como componente da aplicação é distinta do uso do ChatGPT como ferramenta de apoio ao desenvolvimento.

## 6. Reflexão final

O principal aprendizado foi compreender que integrar um modelo de linguagem a uma aplicação exige não apenas preparar e enviar requisições, mas também validar configurações, tratar falhas e avaliar as respostas produzidas.

A competência mais desenvolvida foi a organização e estruturação de aplicações Python, especialmente na separação de responsabilidades, tratamento de exceções e implementação de testes automatizados.

Como aspecto a aprimorar, destaca-se a necessidade de desenvolver mecanismos de validação semântica para avaliar a consistência das respostas geradas pelo modelo.