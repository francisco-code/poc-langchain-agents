from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I'm {name}! What year did {name} win the Nobel Prize?"
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

chain = question_template | model

answer = chain.invoke({"name": "Felipe"})
print(answer.content)