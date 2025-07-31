from langchain_community.document_loaders import PyPDFLoader

def load_resumes(pdf_files):
    all_docs = []
    for file_path in pdf_files:
        docs = PyPDFLoader(file_path).load()
        all_docs.extend(docs)
    return all_docs