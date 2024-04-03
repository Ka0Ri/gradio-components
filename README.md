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

# Blocks

## Event Listeners and Interactivity

- any Component that acts as an input to an event listener is made interactive. However, since Textbox output acts only as an output, Gradio determines that it should not be made interactive
-  If a component is constructed with a default value, then it is presumed to be displaying content and is rendered non-interactive. Otherwise, it is rendered interactive.

## Updating Component Configurations

- Any arguments we do not set will use their previous values.