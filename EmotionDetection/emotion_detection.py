import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=data)

    formated_response = json.loads(response.text)
    
    # Extract emotion scores

# Get the emotion dictionary from the first element in 'emotionPredictions' list
    emotion_dict = formated_response['emotionPredictions'][0]['emotion']

    # Find the emotion with the highest score
    highest_score = max(emotion_dict.values())
    core_emotions = [emotion for emotion, score in emotion_dict.items() if score == highest_score]

    # Print the core emotion(s) and their score

    return core_emotions
