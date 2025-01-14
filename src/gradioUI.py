import gradio as gr
from document_handler import prepare_documents
from model_pipeline import setup_rag_pipeline, query_rag_pipeline

# Charger les documents d'exemple
default_documents = prepare_documents("texts.txt")
rag_pipeline = setup_rag_pipeline(default_documents)

# Fonction pour répondre à une question
def ask_question(query, uploaded_file=None):
    # Si un fichier est uploadé, utilisez son contenu
    if uploaded_file is not None:
        with open(uploaded_file.name, "r") as file:
            custom_documents = prepare_documents(file.name)
        custom_pipeline = setup_rag_pipeline(custom_documents)
        response = query_rag_pipeline(custom_pipeline, query)
    else:
        response = query_rag_pipeline(rag_pipeline, query)
    return response

# Interface Gradio
with gr.Blocks() as rag_interface:
    gr.Markdown(
        """
        # 🧠 RAG Document Assistant
        Posez des questions basées sur des documents !
        - Utilisez les documents d'exemple intégrés.
        - Ou téléchargez vos propres fichiers texte.
        """
    )

    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(
                label="Votre question",
                placeholder="Ex: Combien de demandes de brevets Valeo a-t-il fait en 2022 ?",
            )
            file_upload = gr.File(
                label="Télécharger un fichier (optionnel)",
                file_types=[".txt"],
            )
            submit_button = gr.Button("Poser la question")
        with gr.Column():
            response_output = gr.Textbox(
                label="Réponse générée",
                placeholder="La réponse apparaîtra ici...",
                lines=4,
                interactive=False,
            )
    
    # Ajouter un espace pour des informations supplémentaires
    with gr.Row():
        with gr.Column():
            document_preview = gr.Textbox(
                label="Aperçu du document utilisé",
                placeholder="Contenu du document affiché ici...",
                lines=10,
                interactive=False,
            )
        with gr.Column():
            stats_box = gr.Textbox(
                label="Statistiques",
                placeholder="Score de similarité, temps de réponse, etc.",
                interactive=False,
            )

    # Connecter les composants
    submit_button.click(
        ask_question,
        inputs=[query_input, file_upload],
        outputs=[response_output],
    )

rag_interface.launch()
