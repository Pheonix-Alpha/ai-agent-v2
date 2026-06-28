from langgraph.graph import StateGraph, END

from graph.state import AgentState

from graph.nodes import (
    router_node,
    direct_llm_node,
    calculator_node,
    pdf_node,
    planner_node,
    tool_executor_node,
    synthesize_node,
    route
)

def cache_node(state):
    return {
        **state,
        "answer": state["answer"],
        "route": "cache"
    }


workflow = StateGraph(AgentState)

# Nodes
workflow.add_node(
    "router",
    router_node
)

workflow.add_node("cache", cache_node)

workflow.add_node(
    "direct_llm",
    direct_llm_node
)

workflow.add_node(
    "calculator",
    calculator_node
)

workflow.add_node(
    "search_pdf",
    pdf_node
)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "tool_executor",
    tool_executor_node
)

workflow.add_node(
    "synthesize",
    synthesize_node
)

# Entry
workflow.set_entry_point(
    "router"
)

# Router branching
workflow.add_conditional_edges(
    "router",
    route,
    {
        "cache": "cache",
        "direct_llm": "direct_llm",
        "calculator": "calculator",
        "search_pdf": "search_pdf",
        "planner": "planner"
    }
)

# Simple routes end immediately
workflow.add_edge(
    "direct_llm",
    END
)

workflow.add_edge(
    "calculator",
    END
)

workflow.add_edge(
    "search_pdf",
    END
)

# Planner flow
workflow.add_edge(
    "planner",
    "tool_executor"
)

workflow.add_edge(
    "tool_executor",
    "synthesize"
)
workflow.add_edge("cache", END)
workflow.add_edge(
    "synthesize",
    END
)

app_graph = workflow.compile()