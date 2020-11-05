from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if 'time' in request.GET:
        time = request.GET['time']
        time = int(time)
        if 4 <= time and time < 12:
            result = 'おはようございます!'
        elif 12 <= time and time < 18:
            result = 'こんにちは!'
        elif 18 <= time and time <= 24 or 0 <= time and time < 4:
            result = 'こんばんは!'
        else:
            result = 'Error:Not found TIME!'
        
        return HttpResponse(result)