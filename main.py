import os
from dotenv import load_dotenv
from app import load_resumes, clean_documents, split_documents, create_vectorstore, setup_llm, build_rag_pipeline

load_dotenv()
os.environ["ANONYMIZED_TELEMETRY"] = "False"

#You can add multiple pdfs here
pdf_files = [
    "PDF PATH",
]

def main():
    print("Loading and preparing documents")
    raw_docs = load_resumes(pdf_files)
    cleaned_docs = clean_documents(raw_docs)
    chunks = split_documents(cleaned_docs)

    print("Creating vectorstore")
    vectorstore = create_vectorstore(chunks)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

    print("Initializing LLM")
    llm = setup_llm()
    rag_pipeline = build_rag_pipeline(retriever, llm)

    print("\n System is ready. Ask questions about the resume (type 'exit' to quit).")
    while True:
        query = input("\nQ: ")
        if query.lower() in ['exit', 'quit']:
            break
        answer = rag_pipeline.invoke(query)
        print("A:", answer)

if __name__ == "__main__":
    main()