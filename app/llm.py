from typing import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, MessagesState, StateGraph

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

response = llm.invoke("Tell me a joke about AI")
print(response.content)


class State(MessagesState):
    my_var: str
    customer_name: str


from langchain_core.messages import SystemMessage

system_message = SystemMessage(
    content="You are a helpful assistant that provides information about AI and javascript programing."
)


def node_llm(state: State):
    return {"message": [llm.invoke([system_message] + state["messages"])]}


builder = StateGraph(State)

builder.add_node("node_llm", node_llm)


builder.add_edge(START, "node_llm")
builder.add_edge("node_llm", END)

graph = builder.compile()
