# fie_breast-cancer-prediction
🩺 Breast Cancer Detection & AI Chatbot

This project is a Breast Cancer Detection System combined with an AI Chatbot for symptom analysis. It leverages Google Vision API for image analysis and Google Gemini AI for conversational responses.

🚀 Features

✅ Breast Scan Analysis: Upload two breast scan images (baseline & after 1 month) to analyze possible malignant growth using Google Vision API.
✅ AI Chatbot: Describe symptoms, and the chatbot (powered by Gemini AI) will provide insights.
✅ User-Friendly Interface: Built using Gradio for an interactive web experience.


---

🛠 Setup & Installation

1️⃣ Prerequisites

Python 3.8+

Install the required dependencies:


pip install gradio google-generativeai google-cloud-vision opencv-python numpy

Set up Google Cloud Vision API and download the service account JSON key.

Replace the path to your Google Cloud service account key in the script:


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"PATH_TO_YOUR_JSON_KEY"

Replace GEMINI_API_KEY with your own Google Gemini AI API Key:


GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"


---

🔬 How to Use

1️⃣ Breast Cancer Detection

1. Run the Python script:

python script.py


2. Open the web app in your browser.


3. Upload two breast scan images:

First Scan (Baseline image)

Second Scan (After one month)



4. Click Analyze to detect possible cancerous changes.


5. View the diagnosis result based on the analysis.




---

2️⃣ AI Chatbot for Symptom Analysis

1. Enter your symptoms in the chatbot text box.


2. Click Ask AI to get insights based on Gemini AI.


3. Receive a detailed response about your symptoms.




---

🎯 Technologies Used

Google Cloud Vision API – Image processing & label detection.

Google Gemini AI – AI chatbot for symptom analysis.

Gradio – Web interface for easy interaction.

OpenCV & NumPy – Image preprocessing.



---


💡 Future Enhancements

🔹 Improve image preprocessing for more accurate cancer detection.
🔹 Integrate Real-time Medical Datasets for better predictions.
🔹 Enhance the chatbot with medical NLP models.


---


💙 Developed with the aim of early cancer detection & awareness.
