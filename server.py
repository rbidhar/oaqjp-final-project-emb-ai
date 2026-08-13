from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Handle invalid/blank text
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Format the emotion scores
    emotion_text = ", ".join(
        f"'{key}': {value}"
        for key, value in response.items()
        if key != "dominant_emotion"
    )

    return "For the given statement, the system response is {}. The dominant emotion is {}.".format(
        emotion_text,
        response["dominant_emotion"]
    )


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)