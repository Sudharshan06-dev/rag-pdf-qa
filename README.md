# 📄 PDF Question Answering with RAG and Ollama (phi3:mini)

This project implements a fast, local **RAG (Retrieval-Augmented Generation)** system to answer questions about any uploaded PDF using **Ollama-hosted LLMs** (like phi3:mini).

The system supports **any PDF document**: resumes, research papers, policy documents, etc.

---

## 🚀 Features

- 📄 Upload any PDF and ask context-aware questions
- 🧠 Uses local LLMs via Ollama — no cloud LLM API needed
- ⚡ Fast document chunking and embedding
- 🧩 Vector search using Chroma
- 💬 Smart prompting with LangChain's RAG pipeline

---

## 🛠️ Tech Stack

| Component      | Technology Used                         |
|----------------|------------------------------------------|
| Embeddings     | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store   | `Chroma`                                 |
| PDF Parsing    | `Pypdf`         |
| Local LLM      | `Ollama` with `phi3:mini` |
| Framework      | `LangChain`, `langchain-community`       |

---

## 🧠 Dynamic Prompting

The system uses a flexible prompt template that adapts to the content of the uploaded PDF.

For example:

- If you upload a resume, it can answer:  
  > "What technologies has user worked with?"

- If you upload a research paper, it can answer:  
  > "Summarize the main contributions."

- If you upload a policy doc:  
  > "What are the security guidelines mentioned?"

---

## ⚙️ Setup

```bash
🔧 1. Clone the repo

git clone https://github.com/Sudharshan06-dev/rag-resume.git

🧪 2. Create a virtual environment

python3.11 -m venv venv
source venv/bin/activate

📦 3. Install dependencies

pip install -r requirements.txt

4. 🦙 Ollama Setup

This project runs fully locally using [Ollama](https://ollama.com/), which allows you to run high-performance LLMs on your own machine with no internet required for inference.

# 1. Install Ollama (macOS)
brew install ollama

# 2. Start Ollama in the background (must be running)
ollama serve

# 3. Pull a lightweight model (for fast testing)
ollama pull phi3:mini

🔐 5. Load .env

Ensure this line exists:

# No key needed for Ollama, but you can add other settings here

⸻

▶️ Run the App

python main.py

You’ll see:

✅ System is ready. Ask questions about the document (type 'exit' to quit).
Q:

Start typing questions about the uploaded PDF.

⸻

```

📚 Example Use Cases

- PDF Type	Example Questions
- Resume	“What cloud tools has this person used?”
- Research Paper	“Summarize the methodology section.”
- Company Policy	“What are the leave policies?”
- Technical Manual	“How to configure the database?”


🧠 Future Improvements
- Responsive UI for drag-and-drop file uploads
- File type support beyond PDF (DOCX, Markdown)
- Multi-language support via translation


🧑‍💻 Created By
Sudharshan Madhavan | Final Year M.S. Software Engineering @ CSUF
