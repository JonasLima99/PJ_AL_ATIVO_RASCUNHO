# Projeto de Análise e Automação: Relatório de Alunos Ativos

## Visão Geral

Este projeto pessoal está sendo desenvolvido como um estudo prático usando a base de dados da Secretaria Acadêmica da CESAR School. O objetivo principal é automatizar a geração do relatório de Alunos Ativos utilizando Python e Pandas. Esta é uma aplicação do meu aprendizado em análise de dados, focada em transformar dados brutos em informação útil e confiável.

---

## Contexto de Negócio e Justificativa

### Problema de Negócio

A Secretaria Acadêmica atualmente enfrenta dificuldade em ter uma visualização rápida e precisa do total de estudantes ativos por período. O processo atualmente é manual, lento e exige muito tempo, dificultando o planejamento eficiente.

### Objetivo do Projeto

O objetivo é tratar, limpar e analisar a base de dados de Alunos Ativos (Graduação) do semestre atual, e inicialmente criar um relatório visual que mostre a quantidade de alunos (incluindo matriculados e trancados) separados por período.

### Solução Proposta

Pretendo resolver a dificuldade de visualização criando um relatório visual automático. 

A solução proposta é estabelecer um processo digital que faz três coisas:

* Pega a base de dados bruta, padroniza e trata as informações de alunos ativos.
* Usa as regras de negócio para definir exatamente quem é um aluno "ativo" por período.
* Gera um modelo de relatório que apresenta o quantitativo de alunos de forma clara, facilitando a vida de quem precisa tomar a decisão.

### Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Pandas:** Biblioteca essencial para manipulação e limpeza de dados (foco do aprendizado).
* **gspread / Google APIs:** Utilizadas para a conexão e leitura da base de dados no Google Sheets.
* **Matplotlib/Seaborn:** Serão utilizadas na etapa final para a geração do relatório visual.

### Benefícios

O projeto visa beneficiar diversas áreas da CESAR School, fornecendo dados claros e rápidos.

* **Auxilio na tomada de decisão:** Substituímos o trabalho manual (que pode ter erros) por um processo automático, dando confiança nos números para quem precisa decidir.
* **Melhor Visão:** Permite que as áreas entendam a distribuição dos alunos pelo curso, ajudando a criar um suporte mais personalizado e eficiente para todos.
* **Foco no Futuro:** Ajuda a ter uma ideia das necessidades de demanda e suporte para os próximos semestres.

---

## Estrutura do Projeto

A arquitetura do projeto segue um padrão que facilita a organização do código (separando a leitura, o processamento e a execução).

## Descrição dos Módulos Principais

| Módulo | Função |
| :--- | :--- |
| **`dados/brutos/`** | Contém os arquivos de fonte original. |
| **`dados/tratados/`** | Armazena o DataFrame final, limpo e tratado. |
| **`notebooks/diagnostico.ipynb`** | Ambiente de desenvolvimento para testar funções e entender a base de dados. |
| **`src/carrega_dados.py`** | Responsável por ler o arquivo da pasta brutos/ e carregar os dados no Pandas. |
| **`src/processa_dados.py`** | Contém a lógica de negócio (regras de definições) e realiza a limpeza dos dados. |
| **`src/main.py`** | O comando de execução. Ele chama as funções de carrega_dados.py e processa_dados.py em sequência. |

## Execução do Projeto

Pré-requisitos:

- A base de dados (CSV) deve ser carregada na Planilha Google de destino.
- O arquivo de credenciais (credenciais.json) deve estar na raiz do projeto.
- As bibliotecas Python (pandas, gspread) devem estar instaladas.

...

