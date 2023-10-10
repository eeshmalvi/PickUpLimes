from flask import Flask, render_template, url_for, request
import openai
import os

app = Flask(__name__)

# encrypting the secret key


def decrypt(encrypted_message, key):
    decrypted_chars = []
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - key) % 128)
        decrypted_chars.append(decrypted_char)
    return ''.join(decrypted_chars)


secret_key = 3
encrypted_message = r"vn0nZYyzO6vu\\RI6ksw6YgW6EoenIMkqElXtyY8xemlPtvy\7z"
PickLimesKey = decrypt(encrypted_message, secret_key)


girlInfo = {}
boyInfo = {}
OPENAI_API_KEY = PickLimesKey
openai.api_key = OPENAI_API_KEY


@app.route('/', methods=['GET'])
def index():
    girlInfo.clear()
    boyInfo.clear()
    info = {}
    return render_template('index.html', info=info)


@app.route('/girl', methods=['POST'])
def girlinfo():
    girlInfo["occupation"] = request.form["occupation"]
    girlInfo["hobbies"] = request.form["hobbies"]
    girlInfo["nature"] = request.form["nature"]
    info = {"girlinfo": " Got the Information !!! ",
            "boyinfo": "Required :( ", "result": ""}
    if len(boyInfo) != 0:
        info.update({"girlinfo": " Got the Information !!! ",
                    "boyinfo": " Got the Information !!! "})

    return render_template('index.html', info=info)


@app.route('/boy', methods=['POST'])
def boyinfo():
    boyInfo['pickupline'] = request.form["pickupline"]
    info = {
        "girlinfo": "Required :( ", "boyinfo": "Got the Information !!! ", "result": ""}
    if len(girlInfo) != 0:
        info.update({"girlinfo": " Got the Information !!! ",
                    "boyinfo": " Got the Information !!! "})

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
    output = generate_opinion(girlInfo, boyInfo)
    info = {
        "girlinfo": "Got the Information !!! ", "boyinfo": "Got the Information !!! ", "result": output}
    return render_template('index.html', info=info)


if __name__ == "__main__":
    app.run(debug=True)
