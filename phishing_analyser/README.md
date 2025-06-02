# Analisador de Phishing com IA

Uma ferramenta com interface gráfica moderna que utiliza a API da OpenAI para analisar e-mails e detectar possíveis tentativas de phishing.

<!-- (Substitua esta imagem por um screenshot da sua aplicação em funcionamento) -->
<!-- Exemplo: ![Screenshot da Aplicação](caminho/para/sua/imagem.png) -->

## 📖 Descrição

O **Analisador de Phishing com IA** é uma aplicação de desktop desenvolvida em Python que permite aos utilizadores verificar se um e-mail é uma potencial tentativa de phishing. A ferramenta utiliza o poder dos modelos GPT da OpenAI para analisar o assunto e o corpo do e-mail, fornecendo uma classificação clara (`phishing` ou `nao_phishing`) e uma justificativa detalhada para a análise.

## ✨ Funcionalidades Principais

- **Interface Gráfica Moderna:** Interface de utilizador intuitiva e agradável, construída com a biblioteca `customtkinter`.
- **Análise Detalhada:** Não se limita a classificar; o modelo explica porquê um e-mail é considerado suspeito, apontando táticas como senso de urgência, links falsos e erros de linguagem.
- **Análise de E-mail Único:** Copie e cole o conteúdo de um e-mail para uma análise instantânea.
- **Análise em Lote:** Processe múltiplos e-mails de uma vez, carregando um ficheiro `.csv` com os campos `assunto` e `corpo`.

## ⚙️ Requisitos

- Python 3.7 ou superior
- Conexão com a internet
- Chave de API da OpenAI

## 🚀 Instalação

Siga estes passos para configurar e executar o projeto localmente. É altamente recomendado o uso de um ambiente virtual (`venv`).

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**

    *Windows:*
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    *macOS / Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O ficheiro `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a sua chave de API:**
    Crie um ficheiro chamado `.env` na pasta raiz do projeto e adicione a sua chave da OpenAI:
    ```env
    OPENAI_API_KEY="sua_chave_secreta_aqui"
    ```

## ▶️ Como Usar

Com o ambiente virtual ativado e as dependências instaladas, execute o script principal para iniciar a interface gráfica:

```bash
python phishing_analyser.py
```

-   **Para análise única:** Preencha os campos "Assunto" e "Corpo do E-mail" e clique em "Analisar E-mail".
-   **Para análise em lote:** Clique em "Selecionar Arquivo e Analisar" e escolha um ficheiro `.csv` formatado corretamente (com colunas `assunto` e `corpo`).

## 🔬 Como Funciona

O analisador envia o conteúdo do e-mail para a API da OpenAI com um prompt especializado. Este prompt instrui o modelo (atualmente `gpt-4`) a atuar como um especialista em cibersegurança e a retornar a sua análise num formato JSON estruturado, contendo:

-   `classificacao`: O veredito final ("phishing" ou "nao_phishing").
-   `justificativa`: A explicação detalhada dos elementos que levaram à classificação.

A aplicação processa esta resposta e exibe-a de forma clara na interface.

## 🛠️ Possíveis Melhorias Futuras

- [ ] Integração com clientes de e-mail (Outlook, Gmail) para análise direta.
- [ ] Análise automática de URLs e hashes de anexos.
- [ ] Opções de personalização do modelo de IA e parâmetros de análise na própria interface.
- [ ] Exportação dos resultados da análise em lote para ficheiros (`.csv`, `.txt`, `.pdf`).

## ⚖️ Licença

Este projeto é distribuído sob a licença MIT. Veja o ficheiro `LICENSE` para mais detalhes (se existir, caso contrário, pode adicionar um ficheiro LICENSE.md com o texto da licença MIT).

## ⚠️ Aviso de Segurança

Esta ferramenta é um auxílio educacional e uma camada adicional de verificação. **Não deve ser a sua única linha de defesa contra phishing.** Sempre utilize boas práticas de segurança digital, desconfie de e-mails inesperados e não confie exclusivamente em ferramentas automatizadas para garantir a sua segurança.