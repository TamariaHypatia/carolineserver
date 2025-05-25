from flask import Flask, request
import openai

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'  # Replace this with your real OpenAI API key

@app.route('/', methods=['POST'])
def chat():
    msg = request.form.get('msg', '')

    if not msg:
        return "No message received.", 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}],
            max_tokens=100
        )
        reply = response['choices'][0]['message']['content'].strip()
        return reply
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
