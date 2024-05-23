#pip install azure-ai-textanalytics ​
#https://pypi.org/project/azure-ai-textanalytics/5.1.0/
from azure.core.credentials import AzureKeyCredential 
from azure.ai.textanalytics import TextAnalyticsClient
api_key = "ac2278282be80402fa0cb6163f2579e0cx"
credential = AzureKeyCredential(api_key) 
text_analytics_client = TextAnalyticsClient(endpoint="https://douglasanalisetextoinstancia.cognitiveservices.azure.com/", credential=credential) 
documents = [
    {"id": "1", "language": "pt", "text": "achei este video mais ou menos. Mas acho que não gostei."}, 
    {"id": "2", "language": "pt", "text": "eu adoro passear no parque"}, 
] 
response = text_analytics_client.analyze_sentiment(documents) 
print ("\n\nMeu Resultado: \n\n") 
print (response) 
successful_responses = [doc for doc in response if not doc.is_error]   