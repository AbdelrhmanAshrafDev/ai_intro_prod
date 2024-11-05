# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from transformers import pipeline

# app = Flask(__name__)
# CORS(app)  # This allows CORS for all routes by default

# # Load the text generation pipeline when the API starts
# print("Loading text generation pipeline...")
# generator = pipeline("text-generation", model="gpt2")
# print("Pipeline loaded.")

# @app.route("/generate-text", methods=["POST"])
# def generate_text():
#     # Get the JSON data from the request
#     data = request.get_json()
#     prompt = data.get("prompt")

#     # Validate input
#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400

#     # Run the generator
#     print(f"Running generator with prompt: {prompt}")
#     result = generator(prompt, max_length=300)  # Adjust max_length as needed
#     generated_text = result[0]["generated_text"]
#     print("Generation complete.")

#     # Return the generated text as a JSON response
#     return jsonify({"generated_text": generated_text})

# if __name__ == "__main__":
#     app.run(debug=True)
    
    
    
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the GPTextGenerator class
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

# Initialize the generator instance
text_generator = GPTextGenerator()

@app.route("/generate-text", methods=["POST"])
def generate_text():
    # Get the JSON data from the request
    data = request.get_json()
    prompt = data.get("prompt")
    max_tokens = data.get("max_tokens", 300)  # Optional max_tokens, default to 300

    # Validate input
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Generate the text
    try:
        print(f"Generating text for prompt: {prompt}")
        generated_text = text_generator.generate(prompt, max_tokens=max_tokens)
        print("Text generation complete.")
    except Exception as e:
        print(f"Error during text generation: {e}")
        return jsonify({"error": str(e)}), 500

    # Return the generated text as a JSON response
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(debug=True)