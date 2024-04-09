# gradio-components
Study Custom Gradio components

# 1. Interface
## The 4 Kinds of Gradio Interfaces

It turns out that the gradio.Interface class can actually handle 4 different kinds of demos:

1. **Standard demos**: which have both separate inputs and outputs.
2. **Output-only demos**: which don’t take any input but produce on output. 
3. **Input-only demos**: which don’t produce any output but do take in some sort of input.
4. **Unified demos**: which have both input and output components, but the input and output components are the same. This means that the output produced overrides the input.

<img src=assets\interfaces4.png  />

# 2. Blocks

## Event Listeners and Interactivity

- any Component that acts as an input to an event listener is made interactive. However, since Textbox output acts only as an output, Gradio determines that it should not be made interactive
-  If a component is constructed with a default value, then it is presumed to be displaying content and is rendered non-interactive. Otherwise, it is rendered interactive.

## Updating Component Configurations

- Any arguments we do not set will use their previous values.

# 3. Adding Custom Components

## Adding Custom CSS
- For additional styling ability, you can pass any CSS to your app using the css= kwarg. You can either the filepath to a CSS file, or a string of CSS code.

## Adding custom JavaScript to your demo
There are 3 ways to add javascript code to your Gradio demo:

1. You can add JavaScript code as a string or as a filepath to the js parameter of the Blocks or Interface initializer. This will run the JavaScript code when the demo is first loaded.
2. Events have a js argument that can take a JavaScript function as a string and treat it just like a Python event listener function
3. Lastly, you can add JavaScript code to the head param of the Blocks initializer. This will add the code to the head of the HTML document.

## Adding Custom Components

The Custom Components workflow consists of 4 steps: create, dev, build, and publish.

1. **create**: creates a template for you to start developing a custom component.
2. **dev**: launches a development server with a sample app & hot reloading allowing you to easily develop your custom component
3. **build**: builds a python package containing to your custom component’s Python and JavaScript code — this makes things official!
4. **publish**: uploads your package to PyPi and/or a sample app to HuggingFace Spaces.