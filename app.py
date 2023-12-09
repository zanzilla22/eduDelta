from flask import Flask, request, jsonify, redirect, url_for, render_template, session
from flask import send_file, current_app as app


from flask_cors import CORS
import openai
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from googleapiclient.discovery import build

app = Flask(__name__)
CORS(app)
app.secret_key = 'AIzaSyCMRzuXDIQ9uygtH1oi0zthlYLplMtmt90'

# OAuth 2.0 Configuration
CLIENT_ID = '64555406897-7fc007qom0nt45eunpp2vsc47pdtbrde.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']

# Set your OpenAI API key
openai.api_key = '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'

# Define the GPT-4 model
model_name = 'text-davinci-003'  # Replace with the appropriate GPT-4 model name when available

@app.route('/')
def index():
    return "Hello, prepare to learn with Mr. Zane!"

@app.route('/testAsk')
def ask():
    return render_template("asker.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    # Print the user input for debugging
    print(f"Received message: {user_input}")

    # Make the OpenAI API call using the GPT-4 model
    try:
        response = openai.completions.create(
            model=model_name,
            prompt=user_input,
            max_tokens=150
        )
        # Extract the text response from the OpenAI API response
        text_response = response.choices[0].text.strip() if response.choices else "No response generated."
    except Exception as e:
        print(f"Error: {e}")
        text_response = "An error occurred while generating the response."

    # Print the OpenAI response for debugging
    print(f"Generated response: {text_response}")

    # Return the response to the user
    return jsonify({"response": text_response})

# ------ pdf hosting stuff ------

@app.route('/cr/<string:subject>/<string:grade>')
def show_static_pdf(subject, grade):
    file_path = f'Curicula/{subject}/{subject}-{grade}.pdf'
    print(file_path)  # Use print instead of console.log for server-side code
    return send_file(file_path, mimetype='application/pdf')





# --------- GOOGLE CLASSROOM SHIT --------------
#



if __name__ == '__main__':
    app.run(debug=True)
