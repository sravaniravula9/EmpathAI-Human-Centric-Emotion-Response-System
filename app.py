from flask import Flask, render_template, jsonify
from emotion_detector import detect_emotion
from response_generator import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect")
def detect():
    emotion = detect_emotion()
    response = generate_response(emotion)

    return jsonify({
        "emotion": emotion,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)