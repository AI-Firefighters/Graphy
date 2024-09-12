from langchain.globals import set_debug, set_verbose
set_verbose(True)

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b-instruct-q8_0",
    temperature=0.4,
)