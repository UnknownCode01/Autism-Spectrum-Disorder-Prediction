# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19uctmMlyGAPDASct2k6x5bFMegW20IRY
"""

from flask import Flask, request, jsonify
import openai
import pickle

# Load the trained autism detection model
with open('autism_detector.pkl', 'rb') as model_file:
    autism_detector = pickle.load(model_file)

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "AIzaSyDtCeW3-i_A83s0Wu5qZgmuyJJO6b_MBWI"

# Function to detect autism based on the input features
def detect_autism(input_features):
    """
    Detect autism likelihood based on input features.

    Parameters:
        input_features (list): A list of features for the model.

    Returns:
        str: "Likely" if autism is likely, "Unlikely" otherwise.
    """
    prediction = autism_detector.predict([input_features])
    return "Likely" if prediction[0] == 1 else "Unlikely"

# Function to get a response from the chatbot using OpenAI API
def get_chatbot_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that supports autism detection and provides empathetic guidance."},
            {"role": "user", "content": user_message}
        ]
    )
    return response['choices'][0]['message']['content']

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint to handle chat requests.

    Expects JSON with "message" (user's message) and optionally "features" (for model input).
    """
    data = request.get_json()
    user_message = data.get("message", "")
    input_features = data.get("features", [])

    # Use the model if features are provided
    if input_features:
        model_result = detect_autism(input_features)
        response_message = f"The autism detection result is: {model_result}. How can I assist you further?"
    else:
        # Otherwise, respond as a general chatbot
        response_message = get_chatbot_response(user_message)

    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(port=5000, debug=True)