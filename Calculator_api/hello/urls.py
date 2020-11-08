from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 要調査
    # path('', views.ChoiceView.get, name='ChoiceView.get')
]
