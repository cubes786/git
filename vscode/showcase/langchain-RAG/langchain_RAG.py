import os
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def load_documents_from_csv(filepath):
    """Loads documents from a CSV file, using the 'Text' column as content."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

    # Check if the 'Text' column exists
    if 'Text' not in df.columns:
        print("Error: The CSV file must have a 'Text' column containing the document content.")
        return []

    documents = [
        Document(page_content=row["Text"], metadata={"source": filepath})
        for _, row in df.iterrows()
    ]

    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Splits the documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

csv_filepath = "../../datasets/state_ofthe_union_texts.csv"  # Replace with your datastore filepath
documents = load_documents_from_csv(csv_filepath)
chunks=None


if documents:  # Only proceed if documents were loaded successfully
    chunks = split_documents(documents)

    print(f"Loaded {len(documents)} documents.")
    print(f"Split into {len(chunks)} chunks.")

    # Example: Print the first chunk's content and metadata
    print("\nFirst Chunk Content:")
    print(chunks[0].page_content)
    print("\nFirst Chunk Metadata:")
    print(chunks[0].metadata)
else:
    print("No documents were loaded. Please check the file path and CSV format.")



#create embeddings and store in ChromaDB (vector store)
embedding_model_name = "all-MiniLM-L6-v2"  # A good general-purpose model
def get_or_create_vector_store(chunks, persist_directory="chroma_db", embedding_model_name="all-MiniLM-L6-v2"):   
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

    if os.path.exists(persist_directory) and os.path.isdir(persist_directory):
        try:
            # Attempt to load the existing vector store
            vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
            print("ChromaDB vector store loaded from disk.")
            return vector_store
        except Exception as e:
            print(f"Error loading ChromaDB from disk: {e}. Creating a new one.")
            # If loading fails, create a new one
            vector_store = Chroma.from_documents(
                documents=chunks, embedding=embeddings, persist_directory=persist_directory
            )
            vector_store.persist()
            print("New ChromaDB vector store created and persisted.")
            return vector_store
    else:
        # If the directory doesn't exist, create a new vector store
        vector_store = Chroma.from_documents(
            documents=chunks, embedding=embeddings, persist_directory=persist_directory
        )
        vector_store.persist()
        print("New ChromaDB vector store created and persisted.")
        return vector_store


def create_llm():
    # OpenAI compatible API
    api_base = "http://localhost:1234/v1"  

    llm = OpenAI(
        api_key="N/A",  #  LM Studio doesn't require an API key
        base_url=api_base,
        model_name="deepseek-r1-distill-llama-8b",  # name of your model in LM Studio
        temperature=0.7, # Adjust for more/less randomness
        verbose=True,
        streaming=True,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )
    return llm


def create_rag_chain(llm, vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})  
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # "stuff" is the simplest chain type
        retriever=retriever,
        return_source_documents=True,  #Very helpful for debugging
    )
    return qa_chain


vector_store = get_or_create_vector_store(chunks)
print("ChromaDB vector store is ready.")

llm = create_llm()
rag_chain = create_rag_chain(llm, vector_store)


def query_rag_model(rag_chain, query):
    result = rag_chain.invoke({"query": query})
    return result

#Sample query
query = "What did President Kennedy say about space exploration?"
result = query_rag_model(rag_chain, query)

print("Answer:", result["result"])
print("\nSource Documents:")
for doc in result["source_documents"]:
    print(doc.metadata["source"])