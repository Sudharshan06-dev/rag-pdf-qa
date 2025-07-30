# 🧠 RAG-Resume-QA

A **Retrieval-Augmented Generation (RAG)** application to intelligently answer questions about a candidate’s resume using vector embeddings and a large language model (LLM). This project is built using LangChain, HuggingFace, and ChromaDB.

---

## 📌 Features

- 🔍 Upload multiple resumes and intelligently chunk them
- 🧠 Embed content using `sentence-transformers` (HuggingFace)
- 💬 Ask any question about the resume — get concise, accurate answers
- 🛠️ Powered by RAG: Retrieval + LLM (Zephyr 7B via HuggingFace endpoint)
- 👨‍💻 CLI-based interaction for rapid Q&A

---

## 🛠️ Tech Stack

| Component      | Tech Used                            |
|----------------|--------------------------------------|
| LLM            | HuggingFace Zephyr-7B (HuggingFaceHub) |
| Embeddings     | all-MiniLM-L6-v2 (HuggingFace)       |
| Vector Store   | ChromaDB                             |
| Document Loader| DedocPDFLoader (langchain-community) |
| Framework      | LangChain                            |
| Parsing        | PyPDF2 + Regex                       |

---

## 🧪 Sample Q&A Output

### ✅ Q: *What is Sudharshan's experience with cloud computing?*

**A:**
> Sudharshan has experience working with cloud technologies such as AWS Lambda, API Gateway, SQS, and DynamoDB. He built cloud-native microservices and implemented event-driven architectures using S3 and SNS in a scalable email processing system.

---

### ✅ Q: *Summarize his academic background.*

**A:**
> Sudharshan is pursuing a Master's in Software Engineering at California State University, Fullerton with a GPA of 4.0.

---

---

## 🚀 Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-resume-qa.git
cd rag-resume-qa
```

### 🔐 2. Create a .env File
```bash
HUGGINGFACEHUB_API_TOKEN=your-huggingface-api-token
```

### 📦 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 📄 4. Add Your Resumes
```bash
resume_data/
├── Sudharshan_AI_SoftwareEngineer_Resume.pdf
├── Sudharshan_CloudEngineer_Resume.pdf
...
```
RUN THE APP
```bash
python main.py
```

✅ System is ready. Ask questions about the resume (type 'exit' to quit).
Q:
