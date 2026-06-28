memory = []


def save_chat(role, content):

    memory.append({
        "role": role,
        "content": content
    })


def build_context(limit=10):

    context = ""

    for msg in memory[-limit:]:

        context += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    return context