from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Verificar se a API key está carregada
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Erro: GOOGLE_API_KEY não encontrada no arquivo .env")
    exit(1)

print(f"Usando modelo: gemini-2.5-flash")

# Criar o modelo com o nome correto
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=api_key
)

message = model.invoke("Olá, chatGPT! Qual é a capital da França?")
print("\nResposta:")
print(message.content)