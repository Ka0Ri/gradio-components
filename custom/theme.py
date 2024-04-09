import gradio as gr


with gr.Blocks(css="theme.css") as demo:
    box1 = gr.Textbox(value="Good Job", elem_classes="feedback")
    box2 = gr.Textbox(value="Failure", elem_id="warning", elem_classes="feedback")
    
demo.launch(allowed_paths=["./"])