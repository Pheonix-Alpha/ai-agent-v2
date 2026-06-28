import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="memory"
)

def save_memory(query, answer):

    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[
            f"Q:{query}\nA:{answer}"
        ]
    )

def search_memory(query):

    result = collection.query(
        query_texts=[query],
        n_results=1
    )

    docs = result["documents"][0]

    if docs:
        return docs[0]

    return None