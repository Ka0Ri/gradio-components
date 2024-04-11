import gradio as gr

gr.Interface.load(
             "huggingface/google/vit-base-patch16-224",
             examples=["alligator.jpg", "laptop.jpg"]).launch()