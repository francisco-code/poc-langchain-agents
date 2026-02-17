# 🦜🔗 POC LangChain

Proof of Concept (POC) para explorar os fundamentos do **LangChain** com modelos de linguagem da Google (Gemini) e OpenAI.

## 📋 Descrição

Este projeto demonstra os conceitos básicos do LangChain, incluindo:

- ✅ Integração com Google Gemini (via `langchain-google-genai`)
- ✅ Criação e uso de templates de prompts
- ✅ Chat models com diferentes provedores
- ✅ Gerenciamento seguro de credenciais com `.env`

## 🗂️ Estrutura do Projeto

```
poc-langchain/
│
├── fundamentos.py              # Exemplo básico com ChatGoogleGenerativeAI
├── init-chat-model.py          # Inicialização simplificada de chat models
├── prompt-template.py          # Uso de PromptTemplate básico
├── chat-prompt-template.py     # ChatPromptTemplate com system/user messages
│
├── .env                        # Variáveis de ambiente (credenciais)
├── .gitignore                  # Arquivos ignorados pelo Git
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

## 🚀 Começando

### Pré-requisitos

- Python 3.8+ instalado
- Conta Google Cloud com API Key para Gemini (opcional: OpenAI API Key)

### Instalação

1. **Clone o repositório (ou baixe o projeto)**

```bash
cd poc-langchain
```

2. **Crie e ative um ambiente virtual**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

Edite o arquivo `.env` e insira suas credenciais:

```env
# Google API Key (obrigatório para os exemplos)
GOOGLE_API_KEY=sua_chave_google_aqui

# OpenAI API Key (opcional)
OPENAI_API_KEY=sua_chave_openai_aqui
```

> **⚠️ IMPORTANTE:** Nunca commit suas chaves de API! O `.gitignore` já está configurado para ignorar o arquivo `.env`.

### Obtendo as API Keys

- **Google Gemini API Key**: https://aistudio.google.com/app/apikey
- **OpenAI API Key**: https://platform.openai.com/api-keys

## 📚 Exemplos de Uso

### 1. Fundamentos - Chatbot Básico com Gemini

**Arquivo:** `fundamentos.py`

Exemplo básico de como usar o `ChatGoogleGenerativeAI` com validação de API key:

```bash
python fundamentos.py
```

**Demonstra:**
- Carregamento de variáveis de ambiente com `python-dotenv`
- Validação de credenciais
- Invocação simples de modelo
- Configuração de temperatura

---

### 2. Init Chat Model - Inicialização Simplificada

**Arquivo:** `init-chat-model.py`

Forma mais simples de inicializar um modelo de chat usando `init_chat_model`:

```bash
python init-chat-model.py
```

**Demonstra:**
- API simplificada do LangChain
- Suporte multi-provider (Google, OpenAI, etc.)

---

### 3. Prompt Template - Templates Básicos

**Arquivo:** `prompt-template.py`

Como usar `PromptTemplate` para criar prompts parametrizados:

```bash
python prompt-template.py
```

**Demonstra:**
- Criação de templates reutilizáveis
- Substituição de variáveis em prompts
- Formatação de strings

---

### 4. Chat Prompt Template - Conversas Estruturadas

**Arquivo:** `chat-prompt-template.py`

Como usar `ChatPromptTemplate` para criar conversas com system/user messages:

```bash
python chat-prompt-template.py
```

**Demonstra:**
- System prompts (contexto do assistente)
- User prompts (perguntas do usuário)
- Templates de chat estruturados
- Integração completa com modelo Gemini

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|-----------|--------|-----------|
| **LangChain** | 1.2.10 | Framework para aplicações com LLMs |
| **LangChain Core** | 1.2.13 | Componentes core do LangChain |
| **LangChain Google GenAI** | 4.2.0 | Integração com Google Gemini |
| **Google GenAI** | 1.63.0 | SDK oficial do Google |
| **Python Dotenv** | 1.2.1 | Gerenciamento de variáveis de ambiente |

## 📝 Conceitos do LangChain

### Chat Models

Modelos de linguagem otimizados para conversação:

```python
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5  # 0.0 = determinístico, 1.0 = criativo
)
```

### Prompt Templates

Templates reutilizáveis para prompts:

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I'm {name}!"
)
```

### Chat Prompt Templates

Templates específicos para conversas:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant about {topic}."),
    ("user", "{question}")
])
```

## 🔒 Segurança

- ✅ Arquivo `.env` está no `.gitignore`
- ✅ Credenciais nunca devem ser hardcoded
- ✅ Use variáveis de ambiente para todas as API keys
- ⚠️ **Nunca faça commit do arquivo `.env`**

## 🐛 Troubleshooting

### Erro: "API key not valid"

- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme que a variável se chama exatamente `GOOGLE_API_KEY`
- Certifique-se que não há espaços ou aspas extras na chave

### Erro: "Cannot find reference 'prompts' in 'langchain'"

- Use `from langchain_core.prompts import PromptTemplate` ao invés de `from langchain.prompts`
- Versões recentes do LangChain moveram componentes para `langchain_core`

### Erro: "models/gemini-pro is not found"

- Use `gemini-2.5-flash` ou `gemini-1.5-flash` ao invés de `gemini-pro`
- O modelo `gemini-pro` foi descontinuado na API v1beta

## 📖 Recursos Adicionais

- [Documentação Oficial LangChain](https://python.langchain.com/)
- [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)

## 🤝 Contribuindo

Este é um projeto de estudo. Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto é livre para uso educacional e de estudo.

## ✍️ Autor

**Felipe Correia**

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
