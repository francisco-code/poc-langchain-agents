from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template_translate = PromptTemplate(
    input_variables=["inicial_text"],
    template="Translate the following text to English:\n ```{inicial_text}```"
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```\n\n"
)

llm_en = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

translate = template_translate | llm_en | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

answer = pipeline.invoke({"inicial_text": "LangChain é uma biblioteca de código aberto que facilita a construção de aplicações de linguagem natural. Ela fornece uma interface simples para criar cadeias de processamento, onde cada etapa pode ser um modelo de linguagem, um prompt ou uma função personalizada. Com o LangChain, é possível criar pipelines complexos para tarefas como tradução, resumo, análise de sentimentos e muito mais."})
print(answer)

