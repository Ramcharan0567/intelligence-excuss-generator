from flask import Flask, render_template, request
from utils.excuse_generator import generate_excuse
from utils.proof_generator import generate_proof
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    excuse = ""
    proof_path = ""
    audio_path = ""
    if request.method == 'POST':
        scenario = request.form['scenario']
        urgency = request.form['urgency']

        # Generate excuse
        excuse = generate_excuse(scenario, urgency)

        # Generate proof image
        proof_path = generate_proof(excuse)

        # Generate TTS audio file
        tts = gTTS(text=excuse)
        os.makedirs('static', exist_ok=True)
        audio_path = 'static/excuse.mp3'
        tts.save(audio_path)

    return render_template('index.html', excuse=excuse, proof=proof_path, audio='/' + audio_path)

if __name__ == '__main__':
    app.run(debug=True)
