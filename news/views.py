from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests 

@login_required()
def home(request):
    r = get_news()
    data = {
        "totalResults": r["totalResults"],
        "articles": r["articles"]
    }
    return render(request, 'news.html', data)

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1bf9dd533f64458bbcf95d748e87d15e"
    # headers = {
    #     'Authorization': 'Bearer 1bf9dd533f64458bbcf95d748e87d15e'
    # }
    # response = requests.request("GET", url, headers=headers)
    res = requests.get(url)
    r = res.json()

    return r
