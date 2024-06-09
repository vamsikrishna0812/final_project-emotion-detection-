import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=data)

    response_dict = json.loads(response.text)
    
    # Extract emotion scores
    anger_score = response_dict['anger']
    disgust_score = response_dict['disgust']
    fear_score = response_dict['fear']
    joy_score = response_dict['joy']
    sadness_score = response_dict['sadness']
    
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