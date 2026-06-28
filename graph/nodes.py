from router import route_query
from tools import TOOLS
from planner import create_plan
from executor import llm_call
from rag.retriever import retrieve
from cache.redis_cache import get_cache
from cache.redis_cache import get_cache
from executor import make_cache_key


def router_node(state):

    prompt = state["query"]

    cache_key = make_cache_key(prompt, "")

    cached = get_cache(cache_key)

    if cached:
        # handle both formats safely
        if isinstance(cached, dict):
            value = cached.get("value")
        else:
            value = cached

        return {
            **state,
            "route": "cache",
            "answer": value
        }

    route = route_query(prompt)

    return {
        **state,
        "route": route
    }


def direct_llm_node(state):

    answer = llm_call(
        state["query"]
    )

    return {
        **state,
        "answer": answer
    }


def calculator_node(state):

    answer = TOOLS["calculator"](
        state["query"]
    )

    return {
        **state,
        "answer": answer
    }

def pdf_node(state):

    context = retrieve(
        state["query"]
    )

    prompt = f"""
Answer from the ERP document.

Context:
{context}

Question:
{state['query']}
"""

    answer = llm_call(prompt)

    return {
        **state,
        "answer": answer
    }

def planner_node(state):

    plan = create_plan(
        state["query"]
    )

    print("PLAN:", plan)

    return {
        **state,
        "plan": plan
    }

def tool_executor_node(state):

    results = []

    for step in state["plan"]:

        tool = step.get("tool")

        inp = (
            step.get("input")
            or step.get("expression")
        )

        if tool in TOOLS:

            results.append(
                TOOLS[tool](inp)
            )

    return {
        **state,
        "results": results
    }


def synthesize_node(state):

    prompt = f"""
Use tool results to answer.

Results:
{state['results']}

Question:
{state['query']}
"""

    answer = llm_call(prompt)

    return {
        **state,
        "answer": answer
    }


def route(state):

    return state["route"]



def cache_node(state):
    query = state["query"]

    cached = get_cache(query)

    if cached:
        return {
            **state,
            "answer": cached,
            "route": "cache",
            "cached": True
        }

    return state