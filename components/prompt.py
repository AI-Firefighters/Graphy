from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from jinja2 import Environment, BaseLoader

CALUDE_PROMPT = open("components/anthropic.jinja2", "r", encoding="utf8").read().strip()
env = Environment(loader=BaseLoader())
# generic = env.from_string(CALUDE_PROMPT)
generic = ChatPromptTemplate.from_messages([
    SystemMessage(content=CALUDE_PROMPT),
    ("user", "{query}")
])