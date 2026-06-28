from pypdf import PdfReader

reader = PdfReader(
    "data/erp.pdf"
)

text = ""

for page in reader.pages:

    text += page.extract_text()

def search_pdf(query):

    keywords = query.lower().split()

    matches = []

    for keyword in keywords:

        idx = text.lower().find(keyword)

        if idx != -1:

            matches.append(
                text[
                    max(0, idx - 300):
                    idx + 700
                ]
            )

    if matches:
        return "\n\n".join(matches[:3])

    return "Not found"