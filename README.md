# gradio-components
Study Custom Gradio components

# Interface
## The 4 Kinds of Gradio Interfaces

It turns out that the gradio.Interface class can actually handle 4 different kinds of demos:

1. **Standard demos**: which have both separate inputs and outputs.
2. **Output-only demos**: which don’t take any input but produce on output. 
3. **Input-only demos**: which don’t produce any output but do take in some sort of input.
4. **Unified demos**: which have both input and output components, but the input and output components are the same. This means that the output produced overrides the input.

<img src=assets\interfaces4.png  />