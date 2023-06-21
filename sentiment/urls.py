from django import views
from django.urls import path
from sentiment.views import analyze

urlpatterns = [
    path('analyze/',analyze, name='analyze'),
]
