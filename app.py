from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    language = request.form['language']
    text = request.form['text']
    
    tts = gTTS(text=text, lang=language)
    tts.save('output.mp3')
    os.system('start output.mp3')
    
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
