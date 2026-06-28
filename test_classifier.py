from classifier import classify

questions = [
    "Hello",
    "2 + 2",
    "Summarize ERP from PDF",
    "Compare ERP systems and recommend one"
]

for q in questions:

    print("\nQUESTION:", q)

    print(
        "CLASS:",
        classify(q)
    )