import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_obj, headers=header)

    # If the API returns 400, return None for all values
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # If the API returns 200, process the response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_response = formatted_response["emotionPredictions"][0]["emotion"]

        emotion_response["dominant_emotion"] = max(
            emotion_response,
            key=emotion_response.get
        )

        return emotion_response

    # Handle any unexpected status code
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }