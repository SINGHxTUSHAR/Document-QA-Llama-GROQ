import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

import time
import os
from dotenv import load_dotenv
load_dotenv()


os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")

## embedding using the HuggingFace
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
from langchain_huggingface import HuggingFaceEmbeddings
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

## model selection from the groq API Inference
selected_model = st.sidebar.selectbox(
    "Select Groq Model",
    options=["Llama3-8b-8192", "Llama3-70b-8192", "llama-3.3-70b-versatile",
             "Deepseek-R1-Distill-Llama-70b", "mixtral-8x7b-32768", "Gemma2-9b-It"],
    index=0  # Default selection
)

llm=ChatGroq(groq_api_key=groq_api_key,model_name=selected_model)

## File uploader in the sidebar to upload PDF documents
st.sidebar.markdown("Upload Your PDF Documents")
docs_folder = "Docs"
if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

uploaded_files = st.sidebar.file_uploader(
    "Select PDF files", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(docs_folder, uploaded_file.name)
        # Save the uploaded file to the "Docs" folder
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.sidebar.success("Files uploaded and saved to the Docs folder.")
    
    

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate respone based on the question.
    <context>
    {context}
    <context>
    Question:{input}

    """

)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.loader=PyPDFDirectoryLoader("Docs") 
        st.session_state.docs=st.session_state.loader.load() 
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)
st.title("RAG Document Q&A With Groq And Llama3")

user_prompt=st.text_input("Enter your query from the Docs/Uploaded-Docs")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")


if user_prompt:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)

    start=time.process_time()
    response=retrieval_chain.invoke({'input':user_prompt})
    print(f"Response time :{time.process_time()-start}")
    st.write(response['answer'])
    st.write("Response time :"+str(time.process_time()-start))


    ## With a streamlit expander
    with st.expander("Document similarity Search"):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('------------------------')
