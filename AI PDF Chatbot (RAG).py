import streamlit as st
from groq import Groq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

# -----------------------------
# GROQ API
# -----------------------------
client = Groq(
    api_key="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"
)

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("AI PDF Chatbot (RAG)")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# -----------------------------
# PROCESS PDF
# -----------------------------
if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    # -----------------------------
    # TEXT CHUNKING
    # -----------------------------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    # -----------------------------
    # EMBEDDINGS
    # -----------------------------
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # -----------------------------
    # VECTOR DATABASE
    # -----------------------------
    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    st.success("PDF Processed Successfully!")

    # -----------------------------
    # USER QUESTION
    # -----------------------------
    question = st.text_input(
        "Ask Question From PDF"
    )

    if question:

        # Similarity Search
        retrieved_docs = vectorstore.similarity_search(
            question,
            k=3
        )

        context = "\n".join(
            [doc.page_content for doc in retrieved_docs]
        )

        # -----------------------------
        # PROMPT
        # -----------------------------
        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {question}
        """

        # -----------------------------
        # GROQ LLM
        # -----------------------------
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        answer = response.choices[0].message.content

        st.subheader("Answer")
        st.write(answer)
