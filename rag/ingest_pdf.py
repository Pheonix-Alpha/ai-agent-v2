from pypdf import PdfReader
import chromadb
import uuid

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="erp_docs"
)

reader = PdfReader("data/erp.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

chunks = []

chunk_size = 1000

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i + chunk_size])

for chunk in chunks:

    collection.add(
        ids=[str(uuid.uuid4())],
        documents=[chunk]
    )

print("PDF indexed.")