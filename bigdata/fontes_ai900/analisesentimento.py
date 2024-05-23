#pip install azure-ai-textanalytics
#https://pypi.org/project/azure-ai-textanalytics/5.1.0/
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

api_key = "c2278282be80402fa0cb6163f2579e0c"
credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint="https://douglasanalisetextoinstancia.cognitiveservices.azure.com/", credential=credential)
documents = [
    {"id": "1", "language": "pt", "text": "Algumas pessoas são como vinho: ficam melhor com uma rolha na boca."},
    {"id": "2", "language": "pt", "text": "O cérebro é uma coisa maravilhosa, todos deveriam ter um"},
    {"id": "3", "language": "pt", "text": "Puxa, que bom que o elevador quebrou!"},
    {"id": "4", "language": "pt", "text": "O cérebro é ótimo, todos deveriam ter um"},
]
response = text_analytics_client.analyze_sentiment(documents)
print ("\n\nMeu Resultado: \n\n")
print (response)
successful_responses = [doc for doc in response if not doc.is_error]                                           

