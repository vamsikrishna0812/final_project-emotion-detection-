import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=data)

    formated_response = json.loads(response.text)
    print(response)
    print(formated_response)
    # Extract emotion scores
    anger_score = formated_response['anger']
    disgust_score = formated_response['disgust']
    fear_score = formated_response['fear']
    joy_score = formated_response['joy']
    sadness_score = formated_response['sadness']
    
    # Find the dominant emotion
    emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
emotion_detector("iam so happy iam doing this")