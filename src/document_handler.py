from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter

def prepare_documents(file_path):
    """Load and preprocess documents from a text file."""
    with open(file_path, "r") as file:
        texts = file.readlines()
    
    documents = [Document(page_content=text.strip()) for text in texts]
    
    # Split documents into chunks for efficient retrieval
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    chunked_documents = text_splitter.split_documents(documents)
    
    return chunked_documents
