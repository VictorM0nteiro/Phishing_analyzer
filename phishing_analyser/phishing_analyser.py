import os
from openai import OpenAI
from dotenv import load_dotenv
import sys

# Carrega variáveis do .env
load_dotenv()

def analisar_phishing(assunto, corpo):
    """
    Analisa um e-mail para detectar se é phishing usando a API da OpenAI.
    """
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Erro: Chave da API OpenAI não encontrada no arquivo .env")
            sys.exit(1)

        client = OpenAI(api_key=api_key)

        prompt = f"""
        Analise o seguinte e-mail para determinar se é uma tentativa de phishing.
        Assunto: {assunto}
        Corpo: {corpo}
        Responda apenas com "phishing" ou "não eh phishing".
        """

        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "Você é um especialista em segurança cibernética especializado em detectar e-mails de phishing."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=50
        )

        resultado = response.choices[0].message.content.strip().lower()

        if "phishing" in resultado and ("não" not in resultado and "nao" not in resultado):
            return "phishing"
        else:
            return "não eh phishing"

    except Exception as e:
        print(f"Erro ao chamar API da OpenAI: {e}")
        sys.exit(1)

def main():
    print("=== Analisador de Phishing ===")
    assunto = input("Assunto do e-mail: ")
    print("Corpo do e-mail (Digite duas vezes Enter para finalizar):")

    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)

    corpo = "\n".join(linhas)

    resultado = analisar_phishing(assunto, corpo)

    print("\nResultado da análise:", resultado)

if __name__ == "__main__":
    main()
