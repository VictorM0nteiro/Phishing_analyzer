# Analisador de Phishing

Uma ferramenta de linha de comando que utiliza a API da OpenAI para analisar e-mails e detectar possíveis tentativas de phishing.

## Descrição

O Analisador de Phishing é uma aplicação Python com interface gráfica que permite aos usuários verificar se um e-mail é uma potencial tentativa de phishing. A ferramenta utiliza o modelo GPT da OpenAI para analisar o assunto e o corpo do e-mail, fornecendo uma classificação (phishing ou não phishing) e uma justificativa detalhada.

## Requisitos

- Python 3.7 ou superior (devido ao `customtkinter`)
- Conexão com a internet
- Chave de API da OpenAI

## Instalação

1. Clone este repositório ou baixe os arquivos para sua máquina local

2. Instale as dependências necessárias:

```bash
pip install openai python-dotenv customtkinter
```

3. Crie um arquivo `.env` na raiz do projeto com sua chave de API da OpenAI:

```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como usar

Execute o script principal para iniciar a interface gráfica:

```bash
python phishing_analyser.py
```

A interface gráfica permite:
1. **Análise de E-mail Único:** Insira o assunto e o corpo do e-mail nos campos designados e clique em "Analisar E-mail".
2. **Análise em Lote:** Clique em "Selecionar Arquivo e Analisar" para escolher um arquivo `.csv`. O arquivo deve conter as colunas `assunto` e `corpo`.

O programa irá:
- Analisar o conteúdo usando a API da OpenAI.
- Exibir o resultado da análise (classificação e justificativa) na área de resultados da interface.

## Como funciona

O analisador utiliza um modelo GPT da OpenAI (atualmente configurado para `gpt-4`) para analisar o conteúdo do e-mail. O sistema:

1. Envia o assunto e corpo do e-mail (ou múltiplos e-mails de um arquivo CSV) para a API da OpenAI.
2. Utiliza um prompt especializado que instrui o modelo a identificar características de phishing e a responder em formato JSON com uma `classificacao` e uma `justificativa`.
3. Processa a resposta da API para determinar se o e-mail é uma tentativa de phishing e exibe a justificativa fornecida pelo modelo.

## Teste de conexão

O projeto inclui um script `teste_openai.py` que pode ser usado para verificar se sua chave de API está funcionando corretamente:

```bash
python teste_openai.py
```

## Possíveis melhorias futuras

- Integração com clientes de e-mail
- Análise de URLs e anexos suspeitos (além do texto)
- Opções de personalização do modelo de IA e parâmetros de análise
- Exportação dos resultados da análise em lote para diferentes formatos

## Licença

Este projeto é distribuído sob a licença MIT.

## Aviso de segurança

Esta ferramenta deve ser usada apenas como uma camada adicional de segurança. Sempre utilize boas práticas de segurança digital e não confie exclusivamente em ferramentas automatizadas para detectar ameaças.