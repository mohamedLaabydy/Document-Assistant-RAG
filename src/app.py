from document_handler import prepare_documents
from model_pipeline import setup_rag_pipeline, query_rag_pipeline

def main():
    # Load and prepare documents
    documents = prepare_documents("../data/texts.txt")
    
    # Initialize the RAG pipeline
    rag_pipeline = setup_rag_pipeline(documents)
    
    # Ask a question
    query = "Qui est l'auteur de l'article ?"
    # d'autres questions à poser : 
    """
    Qui est l'auteur de l'article ?
    Quelle est la date de publication de l'article ?
    Combien de demandes de brevets Valeo a-t-il fait en 2022 ?
    Qui est le directeur général de Valeo ?
    Quels sont les quatre domaines de transformation de la mobilité mentionnés par Valeo ?
    Quelle était la position de Valeo dans le classement français en 2021 ?
    """
    response = query_rag_pipeline(rag_pipeline, query)
    
    print(f"Query: {query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
