from django.shortcuts import render
from django.http import HttpResponse
import json

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
        
        params = {
            'time':time,
            'result':result,
        }
        
        # json形式に変換
        json_str = json.dumps(params, ensure_ascii=False, indent=2)
        return HttpResponse(json_str)
        #

        return render(request, 'hello/index.html', params)