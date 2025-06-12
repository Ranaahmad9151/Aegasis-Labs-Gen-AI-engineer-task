from langgraph.graph import StateGraph
from agents.global_orchestrator import global_orchestrator

def run_graph(user_input):
    builder = StateGraph()

    @builder.node("Handle Query")
    def handle_node(state):
        return global_orchestrator(state["input"])

    builder.set_entry_point("Handle Query")
    builder.set_finish_point("Handle Query")

    graph = builder.compile()
    return graph.invoke({"input": user_input})
