from django.shortcuts import render
import requests
import json
from django.http import JsonResponse


from .models import WordInfo

def index(request):
    url = "https://api.datamuse.com/words?ml=greeting&md=d&max=5"

    # 发送API请求并获取响应
    response = requests.get(url)
    # 将API响应解析成JSON格式
    data = json.loads(response.text)
    list_data = [{'word': d['word'], 'defs': d['defs'][0]} for d in data]

    return render(request, 'explore.html', {'data': list_data})