from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser
import os
import time
import subprocess
# ... [Your existing AI assistant code here]

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    user_input = data.get('command')
    response = respond(user_input)  # Use your existing respond function
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
