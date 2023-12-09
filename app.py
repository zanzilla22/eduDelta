from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = 'your_secret_key'

# Define the GPT-4 model
model_name = 'text-davinci-004'  # Replace with the appropriate GPT-4 model name when available

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
        response = openai.Completion.create(
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

if __name__ == '__main__':
    app.run(debug=True)
