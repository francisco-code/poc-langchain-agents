from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

text = """The Nobel Prize is a prestigious international award given annually in several categories, 
including Physics, Chemistry, Medicine, Literature, Peace, and Economic Sciences. It was established 
by the will of Alfred Nobel, a Swedish inventor and philanthropist, in 1895. The Nobel Prizes are awarded 
to individuals or organizations that have made significant contributions to humanity in their respective fields. 
The selection process involves rigorous evaluation by committees of experts, and the winners receive a medal, 
a diploma, and a cash prize. The Nobel Prize has become synonymous with excellence and innovation, recognizing 
groundbreaking achievements that have had a profound impact on society."""

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

# Criar um objeto Document a partir do texto
doc = Document(page_content=text)

# Dividir usando split_documents
chunks = text_splitter.split_documents([doc])

print(f"Total de chunks: {len(chunks)}\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:")
    print(chunk.page_content)
    print("-"*50)
