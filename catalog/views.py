from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import requests
import json


from .models import WordInfo
from .Forms import ContactForm

def explore(request):
    url = "https://api.datamuse.com/words?ml=ocean&md=d&max=5"

    # 发送API请求并获取响应
    response = requests.get(url)
    # 将API响应解析成JSON格式
    data = json.loads(response.text)
    list_data = [{'word': d['word'], 'defs': d['defs'][0]} for d in data]

    return render(request, 'explore.html', {'data': list_data})

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]

        return render(request, 'contact_accepted.html', {"message": message, "sender": sender})

    else:
        form=ContactForm()
        return render(request, 'contact_base.html',{"form":form})

