from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyDep4dP7HrPd3YW_raIdGUVSjt5JhuOWhc")  # Replace this

# Use an accessible model from your list
model = genai.GenerativeModel("models/gemini-1.5-pro")


@app.route("/chatbot1", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        # Generate content directly
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error generating content: {e}")
        return jsonify({"error": "Failed to generate content"}), 500


if __name__ == "__main__":
    app.run(debug=True)
