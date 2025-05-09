# Analisador de Phishing

Uma ferramenta de linha de comando que utiliza a API da OpenAI para analisar e-mails e detectar possíveis tentativas de phishing.

## Descrição

O Analisador de Phishing é uma aplicação Python que permite aos usuários verificar se um e-mail é uma potencial tentativa de phishing. A ferramenta utiliza o modelo GPT da OpenAI para analisar o assunto e o corpo do e-mail, fornecendo uma classificação simples: "phishing" ou "não eh phishing".

## Requisitos

- Python 3.6 ou superior
- Conexão com a internet
- Chave de API da OpenAI

## Instalação

1. Clone este repositório ou baixe os arquivos para sua máquina local

2. Instale as dependências necessárias:

```bash
pip install openai python-dotenv
```

3. Crie um arquivo `.env` na raiz do projeto com sua chave de API da OpenAI:

```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como usar

Execute o script principal:

```bash
python phishing_analyser.py
```

O programa irá:
1. Solicitar o assunto do e-mail
2. Solicitar o corpo do e-mail (pressione Enter duas vezes para finalizar a entrada)
3. Analisar o conteúdo usando a API da OpenAI
4. Exibir o resultado da análise

## Como funciona

O analisador utiliza o modelo GPT-4.1-nano da OpenAI para analisar o conteúdo do e-mail. O sistema:

1. Envia o assunto e corpo do e-mail para a API da OpenAI
2. Utiliza um prompt especializado que instrui o modelo a identificar características de phishing
3. Processa a resposta da API para determinar se o e-mail é uma tentativa de phishing

## Teste de conexão

O projeto inclui um script `teste_openai.py` que pode ser usado para verificar se sua chave de API está funcionando corretamente:

```bash
python teste_openai.py
```

## Possíveis melhorias futuras

- Interface gráfica para facilitar o uso
- Análise mais detalhada com explicação dos motivos da classificação
- Suporte para análise de múltiplos e-mails em lote
- Integração com clientes de e-mail
- Análise de URLs e anexos suspeitos

## Licença

Este projeto é distribuído sob a licença MIT.

## Aviso de segurança

Esta ferramenta deve ser usada apenas como uma camada adicional de segurança. Sempre utilize boas práticas de segurança digital e não confie exclusivamente em ferramentas automatizadas para detectar ameaças.