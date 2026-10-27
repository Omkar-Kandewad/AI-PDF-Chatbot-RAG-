# AI PDF Chatbot (RAG)

## 📌 Project Overview
AI PDF Chatbot is a Python-based application that allows users to upload PDF documents and ask questions about their content. It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant text from the uploaded document and generate answers using a Large Language Model (LLM).

## 🚀 Features
- 📄 Upload and process PDF documents.
- ✂️ Split extracted text into manageable chunks.
- 🧠 Generate text embeddings using Hugging Face.
- 🔍 Retrieve relevant document chunks using FAISS similarity search.
- 🤖 Generate context-aware answers using the Groq API.
- 💬 Interactive chatbot interface built with Streamlit.

## 🛠️ Technologies Used
- Python
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- Groq API
- PyPDF

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

### 2. Install dependencies
```bash
pip install streamlit groq langchain-text-splitters langchain-community langchain-huggingface faiss-cpu pypdf sentence-transformers
```

### 3. Configure your Groq API key
Store your API key securely in an environment variable rather than directly in the Python source code.

### 4. Run the application
```bash
streamlit run "AI PDF Chatbot (RAG).py"
```

## 🔄 How It Works
1. The user uploads a PDF document.
2. PyPDFLoader extracts the document text.
3. LangChain splits the text into smaller chunks.
4. Hugging Face generates embeddings for the chunks.
5. FAISS indexes the embeddings and retrieves relevant content.
6. The retrieved content and user question are sent to the Groq language model.
7. The chatbot displays an answer based on the retrieved context.

## 🎯 Use Cases
- Research paper analysis
- Document question answering
- Study material assistance
- Reports and business document analysis
- PDF-based information retrieval

## 🔮 Future Improvements
- Chat history and multi-turn conversations
- Support for multiple PDF documents
- Source page references in answers
- Improved error handling and document processing
- Secure API key management

## 👨‍💻 Author
Developed as a Python, Generative AI, and Retrieval-Augmented Generation (RAG) project.
</WritingBlock
