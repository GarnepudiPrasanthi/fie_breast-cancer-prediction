import os
import gradio as gr
import base64
import google.generativeai as genai
import io
import cv2
import numpy as np
from google.cloud import vision

# Set the path to the Google Cloud service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\HP\\Desktop\\FIE\\total-media-445910-b2-e2596f982093.json"

# 🔹 Use Your Provided Google Gemini 2.0 Flash API Key
GEMINI_API_KEY = "AIzaSyBfzZ36M-gHqDZnC3Tsh5CwBj1OsN-hSRY"

# 🔹 Configure Google Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# 🔹 Configure Google Vision API Client
vision_client = vision.ImageAnnotatorClient()

# 🔹 Function to Convert Image to Base64
def encode_image(image):
    _, buffer = cv2.imencode(".jpg", image)
    return base64.b64encode(buffer).decode("utf-8")

# 🔹 Function to Analyze Two Breast Scans Using Google Vision API
def analyze_images(img1, img2):
    img1_base64 = encode_image(img1)
    img2_base64 = encode_image(img2)

    # Convert images to Google Vision format
    image1 = vision.Image(content=base64.b64decode(img1_base64))
    image2 = vision.Image(content=base64.b64decode(img2_base64))

    # Run Label Detection
    response1 = vision_client.label_detection(image=image1)
    response2 = vision_client.label_detection(image=image2)

    labels1 = {label.description: label.score for label in response1.label_annotations}
    labels2 = {label.description: label.score for label in response2.label_annotations}

    # Identify Cancer-related Labels
    cancer_terms = ["cancer", "tumor", "malignant", "carcinoma"]
    img1_cancer_score = sum(labels1.get(term, 0) for term in cancer_terms)
    img2_cancer_score = sum(labels2.get(term, 0) for term in cancer_terms)

    # Determine Changes in Cancer Probability
    if img2_cancer_score > img1_cancer_score + 0.2:
        result = "⚠ Possible Malignant Growth Detected. Consult a Doctor."
    else:
        result = "✅ No Significant Cancerous Changes Detected."

    return f"Diagnosis: {result} (Score Change: {round(img2_cancer_score - img1_cancer_score, 2)})"

# 🔹 AI Chatbot for Symptom Analysis
def chatbot(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(user_input)
    return response.text

# 🔹 Gradio Web App Interface
iface = gr.Blocks()

with iface:
    gr.Markdown("# 🩺 Breast Cancer Detection & AI Chatbot")

    # Image Analysis Section
    with gr.Row():
        img1 = gr.Image(type="numpy", label="Upload First Scan (Baseline)")
        img2 = gr.Image(type="numpy", label="Upload Second Scan (After 1 Month)")
    btn = gr.Button("Analyze")
    output_text = gr.Textbox(label="Diagnosis Result")
    
    btn.click(analyze_images, inputs=[img1, img2], outputs=output_text)

    # AI Chatbot Section
    gr.Markdown("## 🗣 Chat with AI Advisor")
    chatbot_input = gr.Textbox(label="Describe your symptoms")
    chatbot_btn = gr.Button("Ask AI")
    chatbot_output = gr.Textbox(label="AI Response")
    
    chatbot_btn.click(chatbot, inputs=chatbot_input, outputs=chatbot_output)

# 🔹 Run the Web App
iface.launch(server_name="localhost", server_port=7860)