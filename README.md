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

### Interactive vs Static
- Gradio will use the interactive version (if available) of a component if that component is used as the input to any event; otherwise, the static version will be used.
- When you design custom components, you must accept the boolean interactive keyword in the constructor of your Python class. In the frontend, you may accept the interactive property, a bool which represents whether the component should be static or interactive.

### The value and how it is preprocessed/postprocessed

- The most important attribute of a component is its value.
- The value that is typically set by the user in the frontend (if the component is interactive) or displayed to the user (if it is static)
- it is also this value that is sent to the backend function when a user triggers an event

Each component does two conversions:

- **preprocess**: Converts the value from the format sent by the frontend to the format expected by the python function. This usually involves going from a web-friendly JSON structure to a python-native data structure, like a numpy array or PIL image. The Audio, Image components are good examples of preprocess methods.
- **postprocess**: Converts the value returned by the python function to the format expected by the frontend. This usually involves going from a python-native data-structure, like a PIL image to a JSON structure.

`Every component must implement preprocess and postprocess methods. In the rare event that no conversion needs to happen, simply return the value as-is. Textbox and Number are examples of this.`

`As a component author, YOU control the format of the data displayed in the frontend as well as the format of the data someone using your component will receive`

### The “Example Version” of a Component

To enable the example view, you must have the following two files in the top of the frontend directory:

- Example.svelte: this corresponds to the “example version” of your component
- Index.svelte: this corresponds to the “regular version”