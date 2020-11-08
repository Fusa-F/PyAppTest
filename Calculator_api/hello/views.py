from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from . import forms

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
        
        # # json形式に変換
        # json_str = json.dumps(params, ensure_ascii=False, indent=2)
        # return HttpResponse(json_str)
        # #

        return render(request, 'hello/index.html', params)

# 要調査
# class ChoiceView(View):
#     def get(self, requset):
#         form = forms.ChoiceForm()
#         form.fields['choice1'].choices = [
#             ('1', '1banme'),
#         ]
#         context = {
#             'form': form
#         }
#         return render(request, 'hello/index.html', context)

# choice_view = ChoiceView.as_view()