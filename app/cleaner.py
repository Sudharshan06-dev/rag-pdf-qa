import re
from langchain.docstore.document import Document

def clean_text(text):
    text = re.sub(r'\n\s*\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def clean_documents(docs):
    cleaned_docs = []
    for doc in docs:
        cleaned = clean_text(doc.page_content)
        cleaned_doc = Document(page_content=cleaned, metadata=doc.metadata)
        cleaned_docs.append(cleaned_doc)
    return cleaned_docs