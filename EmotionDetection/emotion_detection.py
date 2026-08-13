import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_obj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_response = formatted_response["emotionPredictions"][0]["emotion"]
    emotion_response['dominant_emotion'] = max(emotion_response, key=emotion_response.get)
    return emotion_response