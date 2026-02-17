from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I'm {name}! What year did {name} win the Nobel Prize?"
)

text = template.format(name="Felipe")
print(text)
