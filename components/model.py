import os
from components.constants import LANGCHAIN_KEY, MODEL
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"

from langchain.globals import set_debug, set_verbose
set_verbose(True)

from langchain_ollama import ChatOllama
llm = ChatOllama(
    model=MODEL,
    temperature=0.4,
)

# Other providers https://python.langchain.com/v0.2/docs/integrations/chat/

# OpenAI
# from langchain_openai.llms import OpenAI
# llm = OpenAI(openai_api_key=constants.APIKEY)

# Google
# from langchain_google_genai.llms import GoogleGenerativeAI
# os.environ["GOOGLE_API_KEY"] = constants.GOOGLE_API_KEY
# llm = GoogleGenerativeAI(model="gemini-pro")