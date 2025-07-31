from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.prompt_template import resume_prompt

def setup_llm():
    return Ollama(
                model="phi3:mini",
                temperature=0.7,
                num_ctx=2048,       # Context window size
                num_predict=256,    # Max tokens to generate
            )


def build_rag_pipeline(retriever, llm):
    def format_docs(docs):
        return "\n".join(doc.page_content for doc in docs)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | resume_prompt
        | llm
        | StrOutputParser()
    )