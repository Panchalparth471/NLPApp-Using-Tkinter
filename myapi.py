import requests
import json

class API:
    def __init__(self):
      pass 
  
    def sentiment_analysis(self,text):
     url = "https://api.edenai.run/v2/text/sentiment_analysis"


     payload = {
         "response_as_dict": True,
         "attributes_as_list": False,
         "show_original_response": False,
         "providers": "sapling,google,microsoft,emvista,tenstorrent,connexun,ibm,lettria,openai,amazon,nlpcloud",
         "language": "en",
         "text": text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjk0OTZkODYtYjllNi00MzMxLTk5ZTUtYzA4ODlhNmEzNDk3IiwidHlwZSI6ImFwaV90b2tlbiJ9.E0dKH4XFu8ysHlNELBRcfYKdLpjW_ENHv2Su35tOvV4"
     }

     response = requests.post(url, json=payload, headers=headers)
     data= response.json()
     openai_data = data.get('openai', {})
     openai_sentiment = openai_data.get('general_sentiment', 'N/A')
     openai_sentiment_rate = openai_data.get('general_sentiment_rate', 'N/A')
     print(data)
     print(openai_data)
     print(openai_sentiment)
     print(openai_sentiment_rate)
     return '{}->{}'.format(openai_sentiment,openai_sentiment_rate)

    def emotion(self,text):
     url = "https://api.edenai.run/v2/text/emotion_detection"


     payload = {
      "providers": "nlpcloud,vernai",
      "text": text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjk0OTZkODYtYjllNi00MzMxLTk5ZTUtYzA4ODlhNmEzNDk3IiwidHlwZSI6ImFwaV90b2tlbiJ9.E0dKH4XFu8ysHlNELBRcfYKdLpjW_ENHv2Su35tOvV4"
     }

     response = requests.post(url, json=payload, headers=headers)
     data= response.json()
     nlpcloud_data = data.get('nlpcloud', {})
     nlpcloud_data1 = nlpcloud_data.get('items', 'N/A')[0]
     nlpcloud_emotion=nlpcloud_data1['emotion']
     nlpcloud_score=nlpcloud_data1['emotion_score']
     print('{} -> {}'.format(nlpcloud_emotion,nlpcloud_score))
     return '{} -> {}'.format(nlpcloud_emotion,nlpcloud_score)
     
     
    def ner(self,text):
        
     url = "https://api.edenai.run/v2/text/named_entity_recognition"

     payload = {
         "response_as_dict": True,
         "attributes_as_list": False,
         "show_original_response": False,
         "providers": "microsoft,amazon,google,neuralspace,lettria,tenstorrent,ibm,openai,nlpcloud",
         "language": "en",
         "text":text
     }
     headers = {
         "accept": "application/json",
         "content-type": "application/json",
         "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjk0OTZkODYtYjllNi00MzMxLTk5ZTUtYzA4ODlhNmEzNDk3IiwidHlwZSI6ImFwaV90b2tlbiJ9.E0dKH4XFu8ysHlNELBRcfYKdLpjW_ENHv2Su35tOvV4"
     }
     
     response = requests.post(url, json=payload, headers=headers)
     data=response.json()
     openai_data = data.get('openai', {})
     openai_data1 = openai_data.get('items', 'N/A')[0]
     openai_cat=openai_data1['category']
     openai_importance=openai_data1['importance']
     print('{} -> {}'.format(openai_cat,openai_importance))
     return '{} -> {}'.format(openai_cat,openai_importance)