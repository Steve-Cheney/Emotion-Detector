import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        formatted_response = {
                            'anger': emotions['anger'],
                            'disgust': emotions['disgust'], 
                            'fear': emotions['fear'], 
                            'joy': emotions['joy'], 
                            'sadness': emotions['sadness'], 
                            'dominant_emotion': max(emotions, key=emotions.get)}
        return formatted_response
    elif response.status_code == 400:
        formatted_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formatted_response

#print(emotion_detector('I hate working long hours.'))