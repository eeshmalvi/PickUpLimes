import openai
import os
from flask import Flask, render_template_string, request

# Sets the API key for the OpenAI API using the value of the 'OPENAI_API_KEY' environment variable.
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY


def generate_opinion():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": f"By using the pickup line as - you look like my moon - glowing and shining everytime what do you think is her reaction to this pickup line . her occupation is teacher , hobby as painting and nature as introvert. dont reveal you are an AI, just provide opinmion aa a human"
            }
        ])
    return response['choices'][0]['message']['content']


output = generate_opinion()
print(output)


# # This code uses the OpenAI API to generate a tutorial for making a recipe using a list of components provided as an argument.


# def generate_tutorial(components):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant"
#             },
#             {
#                 "role": "user",
#                 "content": f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
#             }
#         ])
#     return response['choices'][0]['message']['content']


# # Create a Flask web application object named app and define a route for the root URL that responds to GET and POST requests
# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# # This code defines a function that generates a tutorial based on user input obtained through a POST request.
# def hello():
#     output = ""
#     if request.method == 'POST':
#         components = request.form['components']
#         output = generate_tutorial(components)
#     return render_template('recipe.html', output=output)

# # This code defines a route for the URL "/generate" that only accepts POST requests.


# @app.route('/generate', methods=['POST'])
# # This code defines a function 'generate' that takes a POST request containing a 'components' field and returns the result of calling the 'generate_tutorial' function with the provided components as input.
# def generate():
#     components = request.form['components']
#     return generate_tutorial(components)


# # This code snippet starts the Flask application if the script is being run directly as the main program, running on the IP address '0.0.0.0' and port number 8080.
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
