# Relatório de Execução — P0: Note Organizer

## 1. Evolução do projeto

### P0 — Básico

**Status: Concluído.**

Foi desenvolvida uma aplicação em Python capaz de receber anotações textuais pelo terminal e utilizar um modelo de linguagem para organizá-las em título, resumo, pontos importantes e ações identificadas.

A implementação contempla:

- Integração com a NVIDIA NIM por meio de requisições HTTP.
- Utilização de um modelo de linguagem configurável por variáveis de ambiente.
- Separação das responsabilidades em módulos.
- Instruções específicas para orientar a organização das anotações.
- Tratamento inicial de erros de entrada e comunicação.
- Testes unitários com simulação da resposta do modelo.
- Documentação de instalação, configuração e execução.

### P0 — Intermediário

**Status: Não iniciado.**

Não foram implementadas funcionalidades correspondentes a este nível nesta versão do projeto.

### P0 — Avançado

**Status: Não iniciado.**

Não foram implementadas funcionalidades correspondentes a este nível nesta versão do projeto.

## 2. Decisões técnicas

### 2.1. Integração direta com a API

- **Decisão:** utilizar requisições HTTP com a biblioteca `requests` para comunicação com a NVIDIA NIM.
- **Alternativa considerada:** utilizar frameworks de agentes ou bibliotecas de abstração de LLM.
- **Justificativa:** manter a implementação simples, compreender diretamente o fluxo de comunicação com a API e evitar dependências desnecessárias para o escopo inicial.

### 2.2. Interface de terminal

- **Decisão:** utilizar o terminal como interface de entrada e saída.
- **Alternativa considerada:** desenvolver uma interface gráfica ou aplicação web.
- **Justificativa:** concentrar o desenvolvimento na integração com o modelo e na organização das anotações, mantendo o escopo compatível com o nível Básico.

### 2.3. Configuração por variáveis de ambiente

- **Decisão:** utilizar um arquivo `.env` para armazenar as configurações de acesso ao serviço.
- **Alternativa considerada:** definir credenciais e parâmetros diretamente no código-fonte.
- **Justificativa:** separar configurações do código e evitar a exposição acidental de credenciais no repositório.

### 2.4. Testes com simulação do serviço externo

- **Decisão:** utilizar `unittest` e `unittest.mock` para testar a lógica do organizador sem realizar chamadas reais à API.
- **Alternativa considerada:** depender exclusivamente de testes que realizassem requisições ao serviço externo.
- **Justificativa:** permitir testes determinísticos, sem depender de conexão com a internet, disponibilidade do serviço ou credenciais válidas.

## 3. Testes e resultados

Os testes foram divididos entre verificações automatizadas, que utilizam simulação, e uma validação manual da integração real.

### 3.1. Testes automatizados

| Teste | Entrada/situação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| Organização de anotação | Texto válido com espaços excedentes | Normalização do texto e encaminhamento ao cliente de LLM | Aprovado |
| Rejeição de anotação vazia | Texto composto apenas por espaços | Lançamento de `ValueError` | Aprovado |

**Resultado da execução:**

```text
Ran 2 tests

OK
```

### 3.2. Validação real da integração

| Teste | Entrada/situação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| Comunicação com a NVIDIA NIM | Anotação enviada com credenciais válidas e modelo configurado | Autenticação, envio da solicitação, recebimento da resposta e apresentação no terminal | Validado manualmente |

A execução manual confirmou o funcionamento do fluxo de comunicação com o serviço externo.

Essa validação não integra a suíte automatizada de testes.

### 3.3. Verificações de falha

Durante o desenvolvimento, também foram consideradas situações como entrada vazia, ausência de configurações e falhas de comunicação com o serviço.

O código contempla tratamento para situações como entrada vazia, ausência de configurações e falhas de comunicação com o serviço. Entretanto, esses cenários ainda não possuem cobertura automatizada abrangente.

## 4. Dificuldades e limitações encontradas

Uma das dificuldades observadas durante a validação manual foi a interpretação de expressões genéricas pelo modelo.

Em uma execução, uma expressão como "vamos lá" foi interpretada como uma possível ação, embora não representasse necessariamente uma tarefa concreta.

As instruções do prompt foram utilizadas para orientar o modelo a preservar o significado original e evitar a criação de informações não mencionadas. Apesar disso, a interpretação ainda pode apresentar inconsistências.

Essa limitação permanece na versão Básica, que não possui uma etapa adicional de validação semântica da resposta.

## 5. Utilização de ferramentas de inteligência artificial

### ChatGPT

- **Ferramenta:** ChatGPT.
- **Tarefas apoiadas:** planejamento da implementação, discussão de decisões técnicas, apoio na estruturação do código, revisão da documentação e organização do relatório.
- **Resultado aproveitado:** orientações para separação de responsabilidades, configuração da integração com o LLM, elaboração de instruções para o modelo e documentação do projeto.
- **Revisões realizadas:** as sugestões foram avaliadas e adaptadas ao escopo e à implementação efetiva da aplicação.
- **Verificação:** o código foi executado localmente, os testes automatizados foram realizados e a integração com a NVIDIA NIM foi validada manualmente.

### NVIDIA NIM

A NVIDIA NIM é utilizada como serviço externo de inferência durante a execução da aplicação. Seu uso como componente da solução é distinto da utilização do ChatGPT como ferramenta de apoio ao desenvolvimento.

## 6. Reflexão final

O desenvolvimento da versão Básica permitiu compreender melhor o processo de integração de aplicações Python com modelos de linguagem por meio de APIs.

Também foram trabalhados conceitos de organização modular, configuração por variáveis de ambiente, tratamento de erros, testes automatizados e controle de versão.

Um dos principais aprendizados foi perceber que a utilização de um LLM exige mais do que enviar um texto e receber uma resposta: é necessário definir instruções claras, avaliar os resultados e reconhecer as limitações da interpretação gerada.

Como aspecto a aprimorar, destaca-se a necessidade de ampliar a cobertura de testes e desenvolver mecanismos que permitam avaliar a consistência das respostas produzidas pelo modelo.

