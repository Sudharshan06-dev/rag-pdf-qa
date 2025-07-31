from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def split_documents(docs):
    identity_doc = Document(page_content="""
    Sudharshan Madhavan is a software engineer currently pursuing a Master's in Software Engineering at California State University Fullerton (GPA: 4.0). His work includes cloud computing, AI-based project management tools, and AWS services.
    """)
    docs.insert(0, identity_doc)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=250,
        length_function=len,
    )
    return splitter.split_documents(docs)