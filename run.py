from transformers import pipeline


class GPTextGenerator:
    def __init__(self, model_name="gpt2", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.generator = None  # Lazy-load the model for faster startup

    def load_model(self):
        if not self.generator:
            print("Loading model...")
            self.generator = pipeline("text-generation", model=self.model_name)
            print("Model loaded successfully.")

    def generate(self, prompt, max_tokens=300):
        self.load_model()
        result = self.generator(prompt, max_length=max_tokens, temperature=self.temperature, num_return_sequences=1, truncation=True)
        generated_text = result[0]["generated_text"]
        return generated_text.strip()



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


if __name__ == "__main__":
    main()
