# Agente de Automação de Testes com IA (Desafio DIO)

## Visão Geral do Projeto

Olá\! Eu acabei de concluir um desafio incrível focado em **Inteligência Artificial Generativa** e **Testes de Software**. O objetivo principal foi construir um **Agente de IA** que automatiza a criação de testes unitários em Python, usando o poder do Azure OpenAI.

### Qual é a ideia?

Este projeto transforma um pedaço de código Python (as funções que queremos testar) em um arquivo de testes (`test_functions.py`) totalmente funcional. O agente atua como um "Engenheiro de Testes de IA", garantindo que eu não precise escrever os testes manualmente\!

### O que eu precisei aprender (Tecnologias-Chave)

  * **Azure OpenAI Service (GPT-4o Mini):** O "cérebro" do agente. É o Modelo de Linguagem Grande (LLM) que analisa o código e gera os testes.
  * **LangChain:** O framework que usei para orquestrar a comunicação entre meu código Python e o LLM. Eu aprendi a usar a abordagem moderna **LCEL (LangChain Expression Language)**.
  * **`pytest`:** A biblioteca que usamos para rodar e validar se os testes gerados pela IA estão corretos.
  * **Prompt Engineering:** A arte de escrever instruções (o *prompt*) para o LLM, garantindo que a saída seja exatamente o código Python limpo e formatado que o `pytest` espera.

-----

## O Caminho do Aprendizado: Como Construir o Agente

Documentar este processo foi crucial para meu aprendizado:

### Passo 1: Configuração do Ambiente e Dependências

1.  **Criação de Ambiente Isolado:** Usei o Anaconda para criar um ambiente virtual (`conda create`) e ativá-lo (`conda activate`), garantindo que todas as dependências do projeto fiquem isoladas.
2.  **Instalação dos Pacotes:** Instalei os pacotes essenciais: `langchain`, `langchain-openai`, `python-dotenv` e `pytest`.

### Passo 2: Configuração Segura das Credenciais

1.  **Uso do `.env`:** Usei o pacote `python-dotenv` para carregar minhas chaves e endpoints do Azure de um arquivo `.env`, mantendo minhas credenciais fora do código-fonte e do GitHub.
2.  **Solução de Erros de Validação:** Encontrei e corrigi um erro comum de validação do Pydantic no LangChain, descobrindo que o nome do parâmetro para a versão da API deve ser **`api_version`** (e não `azure_api_version`). Isso garante que a conexão com o Azure seja estabelecida corretamente.

### Passo 3: Criação da Lógica do Agente (`agent.py`)

1.  **Leitura do Código Fonte:** Criei uma função para ler meu arquivo de exemplo (`functions.py`).
2.  **LCEL:** Aprendi a montar o pipeline moderno do LangChain:
    $$prompt \ | \ llm$$
    Isso substitui o antigo `LLMChain` e torna o código mais eficiente.
3.  **Prompt Otimizado (A Chave do Sucesso\!):** Meu prompt foi aprimorado para ser um **engenheiro de testes rigoroso**. O comando crucial para evitar erros de `NameError` foi:
    ```
    "1. Comece com 'import pytest' seguido pela linha 'from functions import *'..."
    ```
    Isso garante que o arquivo de testes importe as funções que ele precisa testar.

### Passo 4: Validação

1.  **Geração:** O agente executa o pipeline e salva o código de teste puro em `test_functions.py`.
2.  **Correção da Lógica:** Descobri que o Agente gerou um teste para `TypeError` na função `is_even` que não passava, pois meu código-fonte não tinha uma validação explícita. Para garantir que os **testes rodem corretamente** (requisito do desafio), corrigi meu `functions.py` para adicionar essa validação, garantindo 100% de sucesso.
3.  **Verificação Final:** Executei o `pytest` e vi **todos os testes passarem**, confirmando que o agente gerou código funcional e que meu código-fonte é robusto.

-----

