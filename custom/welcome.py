import gradio as gr

def welcome(name):
    return f"Welcome to AISeed, {name}!"

with gr.Blocks(js="welcome-anni.js") as demo:
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()
    inp.change(welcome, inp, out)

demo.launch()