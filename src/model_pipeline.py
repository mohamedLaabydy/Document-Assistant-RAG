from langchain.chains import RetrievalQA
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def setup_rag_pipeline(documents):
    """Sets up the RAG pipeline."""
    # Create embeddings
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = FAISS.from_documents(documents, embedding_model)
    
    # Set up Hugging Face model for generation
    model_name = "google/flan-t5-large"
    hf_pipeline = pipeline("text2text-generation", model=model_name)
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    
    # Create RAG chain
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=index.as_retriever()
    )
    return rag_chain

def query_rag_pipeline(rag_chain, query):
    """Runs a query through the RAG pipeline."""
    return rag_chain.run({"query": query})
