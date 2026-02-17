from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

system = ("You are a helpful assistant that answers questions about the {thema}.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(thema="Nobel Prize", question="What year did Marie Curie win?")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)
response = model.invoke(messages)
print(response.content)