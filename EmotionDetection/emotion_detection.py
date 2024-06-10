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
    if response.status_code == 200:
        emotion_dict = formated_response['emotionPredictions'][0]['emotion']
        #print(emotion_dict)
        # Find the emotion with the highest score
        highest_score = max(emotion_dict.values())
        dominant_emotion = [emotion for emotion, score in emotion_dict.items() if score == highest_score]
        emotion_dict['dominant_emotion'] = dominant_emotion
        # Print the core emotion(s) and their score
        return emotion_dict

    elif response.status_code == 400:
        txt = "invalid text! plese try agian"
        return txt
        #return {'emotionPredictions': [{'emotion': {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}, 'target': '', 'emotionMentions': []}], 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}
    elif response.status_code == 500:
       txt = "invalid text! plese try agian"
       return txt
    