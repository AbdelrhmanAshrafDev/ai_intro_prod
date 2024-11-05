
# AI-based Text generation project

## About Explained file

- from (run.py) file, The final result will be as output text.

![Console display](/assets/images/console.jpg)

- this original logic for the project built

- The content of this file is explained and presented.

## About GUI

- this file (gui.py) compiled with Tkinter gui lib.

![GUI App](/assets/images/gui.jpg)

- the result here will be as simple gui from tkinter lib, you can run as an gui

## About End

- you can see the result with the web app (frontend) when use this file

### How to open
1. clone or copy (end.py) file on the local machine.

2. run the file till see the output like:
    ```text
    Loading text generation pipeline...
    Pipeline loaded.
    * Serving Flask app 'end'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```

3. then go to [GPText generator vue app](https://ai-intro-front-generate-text.vercel.app/)

- then use it, possibly see some problems.

## About Versions

- some versions built while building process for the original project that based on ai


# GPTextGenerator - Text Generation with Hugging Face Transformers

This code provides a simple interface for generating text based on a given prompt using Hugging Face's `transformers` library. It uses the `gpt2` model as the default for text generation, allowing for lazy loading of the model to optimize performance on startup. The `GPTextGenerator` class handles model initialization and text generation with customizable parameters.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)

---

## Installation

To use this script, ensure that you have the following libraries installed:

```bash
pip install transformers torch
```

- `transformers`: Provides the `pipeline` for text generation.
- `torch`: Required by `transformers` for running the model computations.

## Code Explanation

### Imports

```python
from transformers import pipeline
```

The `pipeline` function from Hugging Face’s `transformers` library is used to simplify text generation. It automatically handles model loading, tokenization, and inference.

### GPTextGenerator Class

The `GPTextGenerator` class encapsulates the text generation logic and model loading.

#### Initialization (`__init__` method)

```python
class GPTextGenerator:
    def __init__(self, model_name="gpt2", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.generator = None  # Lazy-load the model for faster startup
```

- `model_name`: Specifies the name of the model to use for text generation (`gpt2` by default).
- `temperature`: Controls the randomness of the generated output (higher values yield more random results).
- `generator`: Initially set to `None` for lazy-loading, meaning the model will load only when needed to speed up startup.

#### Model Loading (`load_model` method)

```python
    def load_model(self):
        if not self.generator:
            print("Loading model...")
            self.generator = pipeline("text-generation", model=self.model_name)
            print("Model loaded successfully.")
```

- Checks if `self.generator` is `None`.
- If `None`, it loads the model by initializing a `pipeline` for `text-generation` with the specified model name (`gpt2`).
- Prints messages to indicate the loading status.

#### Text Generation (`generate` method)

```python
    def generate(self, prompt, max_tokens=300):
        self.load_model()
        result = self.generator(prompt, max_length=max_tokens, temperature=self.temperature, num_return_sequences=1, truncation=True)
        generated_text = result[0]["generated_text"]
        return generated_text.strip()
```

- Calls `self.load_model()` to ensure the model is loaded before generating text.
- Uses `self.generator` to generate text with the following parameters:
  - `prompt`: The input text for generation.
  - `max_length`: Maximum tokens for the generated text (defaults to 300).
  - `temperature`: Randomness level, inherited from the initialization.
  - `num_return_sequences`: Number of generated sequences to return (1 by default).
  - `truncation`: Ensures the output is truncated to the specified `max_length`.
- Returns the generated text with any leading/trailing whitespace removed.

### Main Function

```python
def main():
    # prompt = input("Enter a prompt for the AI to generate text: ").strip()
    prompt = "how are you doing"
    
    if not prompt:
        print("Please enter a valid prompt.")
        return

    # Initialize the text generator
    generator = GPTextGenerator("gpt2")

    # Generate text
    generated_text = generator.generate(prompt)
    print("\nGenerated Text:")
    print(generated_text)
```

- Sets a prompt for text generation.
- Creates an instance of `GPTextGenerator` with the `gpt2` model.
- Calls the `generate` method to produce the generated text, which is then printed to the console.

### Execution Block

```python
if __name__ == "__main__":
    main()
```

This block runs the `main` function when the script is executed directly.

---

## Usage

1. Save the code to a `.py` file (e.g., `text_generator.py`).
2. Run the script.

You can provide a prompt in the `prompt` variable in the `main` function to see the generated text.

---

## Example

Output example when using the prompt `"how are you doing"`:

```text
Loading model...
Model loaded successfully.

Generated Text:
I'm doing well, thank you for asking! How about you?
```

This output may vary depending on the prompt and temperature settings.