from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
OpenAI.api_key = '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'

# Create an OpenAI client instance
client = OpenAI(api_key=OpenAI.api_key)

# Define the assistant ID (replace 'your_assistant_id' with the actual ID)
assistant_id = 'asst_k1bMHyY9Vo0RO7sVZqWRXVg7'

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

    # Make the OpenAI API call using the Assistants API
    response = client.assistants.create_message(
        assistant_id=assistant_id,
        message={
            "role": "user",
            "content": user_input
        }
    )

    # Extract the text response from the OpenAI API response
    text_response = response.get('choices', [{}])[0].get('message', {}).get('content', "No response generated.")

    # Print the OpenAI response for debugging
    print(f"Generated response: {text_response}")

    # Return the response to the user
    return jsonify({"response": text_response})

if __name__ == '__main__':
    app.run(debug=True)
