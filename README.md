# RAG Document Assistant

## Description
The RAG Document Assistant is a Retrieval-Augmented Generation (RAG) system designed to answer questions based on the content of a specific document. It combines retrieval and text generation models to identify the most relevant information and produce coherent, context-aware responses. This system is particularly suited for large, unstructured text data, such as manuals, legal documents, or reports.

For this project, we tested the system on an excerpt from an article written by Emmanuel Egloff in Le Figaro titled Valeo, premier déposant français de brevets en Europe en 2022. The choice of a small excerpt was deliberate, considering the relatively simple and lightweight models employed, such as Flan-T5. Another test was conducted using GPT-2, but it did not yield satisfactory results, which was expected given GPT-2's unidirectional architecture, which limits its performance in tasks requiring contextual understanding.

Flan-T5, on the other hand, delivered good results with the proposed questions. Additionally, I implemented an interactive interface using Gradio, allowing users to upload documents and pose questions interactively.

Future improvements to the system could include testing more robust models like Mistral or Falcon and enhancing the system's efficiency when dealing with more complex documents, such as legal or technical texts.
## Requirements
- Python 3.9 or later
- Docker (optional, for containerized deployment)

## Python Dependencies
The following Python libraries are required:

* langchain
* transformers
* faiss-cpu
* sentence-transformers
* PyYAML
These dependencies are listed in the requirements.txt file.

## Setup Instructions

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t rag-document-assistant .

2. Run the Docker container:
   ```bash
   docker run --rm rag-document-assistant

### Running Locally
If you prefer to run the program locally without Docker:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rag-document-assistant.git
   cd rag-document-assistant

2. Set up a Python virtual environment (optional but recommended): 
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/macOS
   venv\Scripts\activate       # For Windows

3. Install dependencies:
   ```bash
   pip install -r src/requirements.txt

4. Run the application:
   ```bash
   python src/gradioUI.py      # to run the interface 
   python src/app.py           # to run the application

