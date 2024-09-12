from components.model import llm
from components.prompt import generic
from components.tools import tools
from langgraph.prebuilt import create_react_agent

qa_chain = generic | llm

react_chain = create_react_agent(model=llm, tools=tools, state_modifier=generic)