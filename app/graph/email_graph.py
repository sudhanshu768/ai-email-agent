from langgraph.graph import StateGraph, END
from app.nodes.intent_node import intent_node
from app.nodes.summary_node import summary_node
from app.nodes.scheduling_node import scheduling_node
from app.nodes.end_node import end_node


class EmailState(dict):
    pass


def route_intent(state):
    intent = state.get("intent", "").lower().strip()  # ✅ FIX

    if "schedule" in intent:
        return "scheduling"
    elif "summary" in intent:
        return "summary"
    else:
        return "summary"  # fallback


def build_graph():
    graph = StateGraph(EmailState)

    # Nodes
    graph.add_node("intent", intent_node)
    graph.add_node("summary", summary_node)
    graph.add_node("scheduling", scheduling_node)
    graph.add_node("end", end_node)

    # Entry
    graph.set_entry_point("intent")

    # Routing
    graph.add_conditional_edges(
        "intent",
        route_intent,
        {
            "summary": "summary",
            "scheduling": "scheduling",
        }
    )

    # Flow to end node
    graph.add_edge("summary", "end")
    graph.add_edge("scheduling", "end")

    # Final
    graph.add_edge("end", END)

    return graph.compile()