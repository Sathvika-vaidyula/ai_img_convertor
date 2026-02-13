 AI Image Generator
Overview

 AI Image Generator is a web application that allows users to generate images from text prompts using the Hugging Face Inference API.

Users can:

Enter a text prompt

Generate AI-powered images

View results instantly

Download generated images

The application features a clean, modern UI with smooth animations for an enhanced user experience.

 Features

 Text-to-Image Generation using Hugging Face models

 Fast API Integration with Hugging Face Inference API

 Download Generated Images

 Dynamic Gradient Background Animation

 Responsive and Interactive UI

 Secure API Key Handling using Environment Variables

Tech Stack

Backend

Python

Flask

Frontend

HTML

CSS

JavaScript

API

Hugging Face Inference API

 Project Structure
ai-image-generator/
│
├── static/
│   └── styles.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

 Prerequisites

Before running the project, make sure you have:

Python 3.7+

pip installed

Hugging Face API token

 Installation
1️⃣ Clone the Repository
git clone https://github.com/Sathvika-vaidyula/ai_img_convertor.git
cd ai_img_convertor

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

 Configuration (IMPORTANT)

Create a .env file in the root directory:

HF_TOKEN=your_huggingface_api_token_here


Never hardcode your API key in app.py.

The application securely loads the token using environment variables.

▶️ Running the Application

Start the Flask server:

python app.py


Open your browser:

http://127.0.0.1:5000


Enter a prompt and generate images 

 requirements.txt

If missing, generate using:

pip freeze > requirements.txt

 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

git checkout -b feature-name


Commit your changes

git commit -m "Add feature-name"


Push to your branch

git push origin feature-name


Create a Pull Request

 License

This project is licensed under the MIT License.

Acknowledgements

Hugging Face for providing the Inference API

Flask Documentation

Open-source community

Author

Sathvika Vaidyula

GitHub: https://github.com/Sathvika-vaidyula



Live Deployment instructions

Screenshot preview section

Portfolio-style formatting
