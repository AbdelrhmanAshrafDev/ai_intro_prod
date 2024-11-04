

from transformers import pipeline
import tkinter as tk
from tkinter import filedialog

class GPTextGenerator:
    def __init__(self, model_name="gpt2", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.generator = None  # Lazy-load the model for faster app startup

    def load_model(self):
        if not self.generator:
            print("Loading model...")
            self.generator = pipeline("text-generation", model=self.model_name)
            print("Model loaded successfully.")

    def generate(self, prompt, max_tokens=300, max_steps=5):
        self.load_model()
        generated_text = prompt
        for _ in range(max_steps):
            result = self.generator(generated_text[-max_tokens:], 
                                    max_length=max_tokens, 
                                    temperature=self.temperature, 
                                    num_return_sequences=1)
            new_text = result[0]["generated_text"]
            if len(new_text) <= len(generated_text):  # Check for natural stop
                break
            generated_text = new_text
        return generated_text

class TextGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Text Generator")

        self.model = GPTextGenerator("gpt2")  # Load a more advanced model if desired
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Prompt:").pack()
        self.prompt_entry = tk.Entry(self.root, width=50)
        self.prompt_entry.pack(pady=5)

        tk.Label(self.root, text="Generated Text:").pack()
        self.output_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=10)
        self.output_text.pack(pady=5)

        tk.Button(self.root, text="Generate Text", command=self.on_generate).pack(pady=5)
        tk.Button(self.root, text="Clear Text", command=lambda: self.output_text.delete(1.0, tk.END)).pack(pady=5)
        tk.Button(self.root, text="Save to File", command=self.save_text).pack(pady=5)

    def on_generate(self):
        prompt = self.prompt_entry.get().strip()
        if not prompt:
            self.output_text.insert(tk.END, "Please enter a prompt.\n")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Generating text...\n")
        self.root.update()

        generated_text = self.model.generate(prompt)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, generated_text)

    def save_text(self):
        text = self.output_text.get(1.0, tk.END).strip()
        if not text:
            self.output_text.insert(tk.END, "Nothing to save!\n")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextGeneratorApp(root)
    root.mainloop()
