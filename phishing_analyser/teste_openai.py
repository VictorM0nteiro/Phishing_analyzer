import openai
import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Erro: API Key não encontrada!")
    exit(1)

# Configura a chave
openai.api_key = api_key

try:
    # Faz uma requisição simples para listar os modelos disponíveis
    models = openai.models.list()
    print("Conexão bem-sucedida! Modelos disponíveis:")
    for model in models.data[:5]:  # Mostra só os 5 primeiros para não poluir
        print(f"- {model.id}")
except Exception as e:
    print(f"Erro ao conectar na OpenAI: {e}")
