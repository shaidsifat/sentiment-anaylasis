

# Create your models here.
from django.db import models

class SentimentAnalysisResult(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)