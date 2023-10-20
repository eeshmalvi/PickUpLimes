
from flask import Flask, render_template, url_for, request
import openai
import os

app = Flask(__name__)


def decrypt(encrypted_message, key):
    decrypted_chars = []
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - key) % 128)
        decrypted_chars.append(decrypted_char)
    return ''.join(decrypted_chars)


secret_key = 3
encrypted_message = r"vn0nZYyzO6vu\\RI6ksw6YgW6EoenIMkqElXtyY8xemlPtvy\7z"
pickLimesKey = decrypt(encrypted_message, secret_key)


girlInfo = {}
boyInfo = {}
result = ""

OPENAI_API_KEY = pickLimesKey
openai.api_key = OPENAI_API_KEY


@app.route('/', methods=['GET'])
def index():
    girlInfo.clear()
    boyInfo.clear()
    result = ""
    info = {
        "girlinfo": girlInfo,
        "boyinfo": boyInfo,
        "result": result
    }
    return render_template('index.html', info=info)


@app.route('/girl', methods=['POST'])
def girlinfo():
    girlInfo["occupation"] = request.form["occupation"]
    girlInfo["hobbies"] = request.form["hobbies"]
    girlInfo["nature"] = request.form["nature"]

    info = {
        "girlinfo": girlInfo,
        "boyinfo": {},
        "result": ""
    }

    if len(boyInfo) != 0:
        info["boyinfo"] = boyInfo

    return render_template('index.html', info=info)


@app.route('/boy', methods=['POST'])
def boyinfo():
    boyInfo['pickupline'] = request.form["pickupline"]
    info = {
        "girlinfo": {},
        "boyinfo": boyInfo,
        "result": ""
    }
    if len(girlInfo) != 0:
        info["girlinfo"] = girlInfo

    return render_template('index.html', info=info)


def generate_opinion(girlInfo, boyInfo):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": f" By using the pickup line as - {boyInfo['pickupline']}. What do you think is her reaction to this pickup line . Her profession is {girlInfo['occupation']} , hobby as {girlInfo['hobbies']} and nature as {girlInfo['nature']}. Don't reveal you are an AI, just provide opinion as a loveguru. Answer sholud be to the point and fun to read"
            }
        ])
    return response['choices'][0]['message']['content']


@app.route('/result', methods=['POST'])
def getresult():
    info = {
        "girlinfo": {},
        "boyinfo": {},
        "result": ""
    }

    if len(girlInfo) != 0:
        info["girlinfo"] = girlInfo

    if len(boyInfo) != 0:
        info["boyinfo"] = boyInfo

    if len(girlInfo) != 0 and len(boyInfo) != 0:
        output = generate_opinion(girlInfo, boyInfo)
        info["result"] = output

    return render_template('index.html', info=info)


if __name__ == "__main__":
    app.run(debug=True)
