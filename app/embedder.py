from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def create_vectorstore(docs, persist_dir=None):
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return Chroma.from_documents(documents=docs, embedding=embedding_model, persist_directory=persist_dir)