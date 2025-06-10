from flask import Flask, request
import openai
import os
import traceback

app = Flask(__name__)

Use environment variable for API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

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
    return "The AI is currently offline for maintenance, but I'm still glowing for you!"
    except Exception as e:
        app.logger.error("Full exception below:")
        app.logger.error(str(e))
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
