# Loading data
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

documents = GenericLoader.from_filesystem(
    ".",
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf8-encoding.py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
).load()

# Chunking the data
# chunks = SemanticChunker(embeddings).split_documents(documents)
chunks = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
).split_documents(documents)

# Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# VectorDB
# from langchain_community.vectorstores import FAISS as DB
from langchain_community.vectorstores import Chroma as DB

# Retriever
db = DB.from_documents(embedding=embeddings,
                       documents=chunks).as_retriever(#)
    search_type="mmr", # "similarity" (default), "mmr", "similarity_score_threshold"
    search_kwargs={"k": 8})