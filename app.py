from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return "Hello, prepare to learn with Mr. Zane!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    response = openai.Completion.create(
        model="g-XYYou3Ysq-hacktheridge", 
        prompt=user_input,
        max_tokens=150
    )

    text_response = response.choices[0].text.strip() if response.choices else "No response generated."

    return jsonify({"response": text_response})

if __name__ == '__main__':
    app.run(debug=True)
