from typing import Annotated, List, Sequence, TypedDict
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END
import operator
from components.chains import qa_chain, react_chain

class AgentState(TypedDict):
    input: str
    answer: str
    # steps: List[str]
    # messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str

def simple_chain(state: AgentState):
    result = qa_chain.invoke(state["input"])
    return {
        "input": "",
        "answer": result
    }

def react_agent(state: AgentState):
    result = react_chain.invoke({"messages": [("human", state["input"])]})
    return {
        "input": "",
        "answer": result
    }


builder = StateGraph(AgentState)

# Define Nodes
builder.add_node("node_1", node_1)

# Connect Node to form a graph
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

# Compile
graph = builder.compile()