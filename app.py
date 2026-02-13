from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
from io import BytesIO
import base64
import os

app = Flask(__name__)


API_KEY = os.getenv("HF_KEY")

client = InferenceClient(token=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    prompt = request.form.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Public lightweight model
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        # Convert image to base64
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return jsonify({"image": img_str})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
