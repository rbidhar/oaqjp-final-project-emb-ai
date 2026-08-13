"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the text submitted by the user and return the emotion."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    emotion_text = ", ".join(
        f"'{key}': {value}"
        for key, value in response.items()
        if key != "dominant_emotion"
    )

    return (
        f"For the given statement, the system response is {emotion_text}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    