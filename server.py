"""
    THIS MY FINAL PROJECT
"""

from flask import Flask ,request ,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """" PERFORMS EMOTION DETECTION """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)


    return response

@app.route("/")
def render_index_page():

    """ DIRECTS TO INDEX.HTML """

    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
