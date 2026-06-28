from graph.workflow import app_graph

result = app_graph.invoke(
    {
        "query":
        "Summarize ERP from PDF and explain benefits"
    }
)

print(result)