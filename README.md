1)Intelligent Excuse Generator

A fun and functional web app that generates smart excuses based on a selected scenario and urgency level. It also creates a text-based proof image and reads the excuse aloud using text-to-speech (TTS).

2)Features
->Scenario-based excuse generation (Work, School, Social)
->Select urgency level (Low, Medium, High)
-> Automatically generates a proof image with the excuse
-> Converts excuse to voice using Google Text-to-Speech (gTTS)
-> Clean and responsive HTML/CSS design
-> Built using Python + Flask

3)Project Structure

intelligent-excuse-generator/
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── style.css
│ ├── excuse.mp3
│ ├── proof.png
│ └── favicon.ico
├── utils/
│ ├── excuse_generator.py
│ └── proof_generator.py
└── README.md

4)Requirements
Python 3.x
Flask
gTTS (Google Text-to-Speech)
Pillow (for image generation)

5)Install with:
bash
pip install flask gtts pillow

6)How to Run
->Clone or download the project folder.
->Open terminal in the project directory.
->Run the Flask app:
  python app.py
->Open browser and visit:
  http://127.0.0.1:5000

7)Usage
->Choose a scenario (Work / School / Social).
->Choose urgency level (Low / Medium / High).
->Click Generate Excuse.
->View the excuse, listen to the voice playback, and see the generated proof image.

8)Sample Output
->excuse: “I had a minor internet issue this morning.”
->Voice playback (MP3)
->Proof image with excuse text

9)Author
Created by [M Sri Ram charan]
Feel free to modify and enhance!

License
MIT License – use freely, improve endlessly.
Let me know if you want me to:
->Add your name to the Author section
->Zip everything into a download
- >Help you host it online for demo purposes

 You're now ready to submit or deploy this project!

