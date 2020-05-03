import json
from flask import Flask, request, make_response, render_template, Response
app = Flask('chatbot')


from utils.service import GetInfo


@app.route('/text', methods=['POST'])
def process_text():
    text = request.json['text']

    info = GetInfo(text)
    data = {
        'info': info,
    }
    js = json.dumps(data)
    return js


@app.route('/')
def index():
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'), 200, headers)


@app.route('/greet')
def say_hello():
    return 'Hello from Server'


if __name__ == "__main__":        # on running python app.py
    app.run()