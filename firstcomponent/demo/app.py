
import gradio as gr
from gradio_firstcomponent import firstComponent


example = firstComponent().example_value()

demo = gr.Interface(
    lambda x:x,
    firstComponent(),  # interactive version of your component
    firstComponent(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
