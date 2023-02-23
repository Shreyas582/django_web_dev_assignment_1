from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests 
from dotenv import load_dotenv
import os
load_dotenv()

@login_required()
def home(request):
    r = get_news()
    data = {
        "totalResults": r["totalResults"],
        "articles": r["articles"]
    }
    return render(request, 'news.html', data)

def get_news():
    API_KEY = os.getenv('API_KEY')
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + API_KEY
    res = requests.get(url)
    r = res.json()

    return r
