from typing import TypedDict


class AgentState(TypedDict, total=False):

    query: str

    route: str

    plan: list

    results: list

    answer: str

    verified: str