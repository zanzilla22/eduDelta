from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
OpenAI.api_key = 'key_here'

# Create an OpenAI client instance
client = OpenAI(api_key=OpenAI.api_key)

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

    # Make the OpenAI API call using the client instance
    response = client.completions.create(
        model="asst_k1bMHyY9Vo0RO7sVZqWRXVg7",
        prompt=user_input,
        max_tokens=150
    )

    # Extract the text response from the OpenAI API response
    text_response = response.choices[0].text.strip() if response.choices else "No response generated."

    # Print the OpenAI response for debugging
    print(f"Generated response: {text_response}")

    # Return the response to the user
    return jsonify({"response": text_response})

if __name__ == '__main__':
    app.run(debug=True)
