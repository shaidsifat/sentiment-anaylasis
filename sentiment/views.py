from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from .models import SentimentAnalysisResult
from transformers import pipeline
from textblob import TextBlob
from setfit import SetFitModel




def perform_sentiment_analysis(text):

    model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
    sentiment = model([text])
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"






@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            data = request.POST
            text = data['text']
            # Call the pre-trained model API or library to perform sentiment analysis
            sentiment = perform_sentiment_analysis(text)
            # Save the result in the database
            result = SentimentAnalysisResult.objects.create(text=text, sentiment=sentiment)
            # Return the sentiment analysis result as JSON response
            return JsonResponse({'sentiment': sentiment})
        except KeyError:
            return JsonResponse({'error': 'Invalid request payload'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
