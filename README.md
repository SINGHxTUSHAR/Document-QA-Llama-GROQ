[![GitHub license](https://img.shields.io/github/license/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg)](https://github.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


[![GitHub watchers](https://img.shields.io/github/watchers/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/network/)
[![GitHub stars](https://img.shields.io/github/stars/SINGHxTUSHAR/Document-QA-Llama-GROQ.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/stargazers/)

[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/SINGHxTUSHAR/Document-QA-Llama-GROQ)


# Document-QA-Llama-GROQ 🤖:

![Preview Image](https://github.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/blob/0358cb8e662057e15ff8c48482a55c44e04f77b0/preview.png)

Document-Q&A using the GROQ and Llama3 is a sophisticated question-answering system designed to retrieve and process information from PDF documents interactively. The project leverages a Retrieval Augmented Generation (RAG) approach by integrating vector embeddings, similarity search, and language model inference. By combining the strengths of Streamlit for the user interface, LangChain for orchestration, and the GROQ API for model inference, the project provides users with a seamless experience for querying document contents.

## Design and Architecture:

`1. User Interface with Streamlit:`
* Interactive Dashboard: The application is built using Streamlit, which offers an intuitive and interactive web interface. Users can upload PDF documents directly from the sidebar and enter their queries in a text input field.
* Dynamic Model Selection: A sidebar dropdown allows users to select from various GROQ inference models (e.g., "Llama3-8b-8192", "Llama3-70b-8192", etc.), providing flexibility based on desired performance or resource constraints.

`2. Document Loading and Processing:`
* PDF Upload and Storage: Uploaded PDF files are saved into a designated directory ("Docs"). This directory serves as the central repository from which documents are loaded.
* Document Loader: The project uses PyPDFDirectoryLoader from the LangChain community package to load the PDFs. This component reads the content of each document and prepares it for further processing.

`3. Text Splitting and Embedding`
* Text Splitting: To manage large documents and maintain context, the project employs a RecursiveCharacterTextSplitter. This tool breaks down documents into smaller, manageable chunks (with a default chunk size of 1000 characters and an overlap of 200 characters), ensuring that important context is preserved across chunks.
* Embedding Generation: Each document chunk is transformed into a vector representation using the HuggingFace model ("all-MiniLM-L6-v2"). These embeddings capture the semantic meaning of the text, facilitating efficient similarity searches.
* Vector Database: The FAISS (Facebook AI Similarity Search) vector store is used to index these embeddings. This enables rapid retrieval of contextually similar document chunks based on user queries.


`4. Query Processing and Answer Generation`
* Prompt Template: A custom ChatPromptTemplate defines the structure for generating responses. The template instructs the language model to answer questions using only the provided context, ensuring that responses remain grounded in the source documents.
* Retrieval Chain: When a user submits a query, the system first performs a similarity search over the vectorized document chunks using FAISS. The most relevant chunks are then fed into a retrieval chain that combines these documents with the user query.
* Language Model Inference: The final answer is generated using the selected GROQ model via the ChatGroq interface. The system computes and displays the response along with the retrieval context for transparency.

## Workflow and Examples:
`Example 1: Uploading Documents and Preparing the Database`
* PDF Upload: Users navigate to the sidebar and upload one or more PDF documents.
* Vector Embedding Creation: By clicking the "Document Embedding" button, the system processes the uploaded documents:
  * The PDFs are loaded from the "Docs" folder.
  * The text is split into chunks.
  * Embeddings are generated using HuggingFace and stored in the FAISS vector store.
* Confirmation: The interface confirms that the vector database is ready for query processing.

`Example 2: Querying and Retrieving Answers`
* User Query: A user enters a query such as "What are the key findings in the uploaded research papers?"
* Document Retrieval: The system retrieves relevant chunks from the vector store based on the query.
* Answer Generation: The retrieved context is combined with the query using the predefined prompt template. The selected GROQ model (e.g., "Llama3-8b-8192") generates an accurate and contextually grounded response.
* Results Display: The answer is displayed on the main page, and users can optionally expand a section to view the retrieved document chunks for further inspection.


## Technical Components and Dependencies:
* Streamlit: Used for building the interactive web interface.
* LangChain Modules:
  * ChatGroq: Connects to the GROQ API for language model inference.
  * HuggingFaceEmbeddings: Generates semantic embeddings using the "all-MiniLM-L6-v2" model.
  * RecursiveCharacterTextSplitter: Splits documents into manageable text chunks.
  * FAISS: Indexes embeddings to enable fast similarity searches.
  * PyPDFDirectoryLoader: Loads PDF documents from a specified directory.
* Environment Variables:
  * GROQ_API_KEY: Used for authenticating with the GROQ API.
  * HF_TOKEN: Token required for HuggingFace services.
* Additional Libraries:
  * dotenv: Manages environment variables.
  * time and os: Handle performance measurement and file operations.
 
## Requirements💻 :

Ensure you have the following dependencies installed:

- Python (version 3.10)
- IDE: VS-CODE or collab
- Virtual-environment(venv)
- Other dependencies (refer to the requirements.txt)

You can install the required Python packages using:

```bash
pip install -r requirements.txt
```


## Setup 💿:

- Clone the repository:
```bash
git clone https://github.com/SINGHxTUSHAR/Document-QA-Llama-GROQ.git
cd Document-QA-Llama-GROQ
```
- Create a virtual environment (optional but recommended):
```
conda create -p venv
```
- Activate venv
```
conda activate venv/
```

## Contributing 📌:
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process. Contributions, issues, and feature requests are welcome!

## Suggestion 🚀: 
If you have any suggestions for me related to this project, feel free to contact me at tusharsinghrawat.delhi@gmail.com or <a href="https://www.linkedin.com/in/singhxtushar/">LinkedIn</a>.

## License 📝:
This project is licensed under the <a href="https://github.com/SINGHxTUSHAR/Document-QA-Llama-GROQ/blob/main/LICENSE">MIT License</a> - see the LICENSE file for details.
