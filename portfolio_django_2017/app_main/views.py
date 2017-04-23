# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text
import requests
from django.http import JsonResponse
from portfolio_django_2017.settings import STATIC_URL
from django.db import transaction


# Главная страница:
class MainListView(ListView):
    # model = MainText
    queryset = MainHeader1Text.objects.order_by('ordinal').\
        prefetch_related('mainheader2text_set',
                         'mainheader2text_set__mainheader3text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set__maintext_set')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # создаю сессию для подрузки данных Ajax-ом только для своих
        # посетителей:
        self.request.session['session_exist'] = True
        return context


def weather_json(request):
    with transaction.atomic():
        # This code executes inside a transaction.
        pass

    content = {}
    if 'session_exist' in request.session:
        try:
            url = 'http://api.wunderground.com//api/d3de2d8a8d6e227e/' \
                  'geolookup/conditions/forecast/lang:RU/q/Russia/' \
                  'Saint Petersburg.json'
            response = requests.get(url)
            image = response.json()["current_observation"]["icon_url"]
            image = image.replace('http://', 'https://')
            temperature = response.json()["current_observation"]["temp_c"]
            text = response.json()["current_observation"]["weather"]
            content['weather_image'] = image
            content['weather_temperature'] = temperature
            content['weather_text'] = text
        except Exception as err:
            content['weather_image'] = STATIC_URL + 'general/img/empty.gif'
            content['weather_temperature'] = ''
            content['weather_text'] = 'Получить погоду не удалось: '  # + err
        return JsonResponse(content)
    content['weather_image'] = ''
    content['weather_temperature'] = ''
    content['weather_text'] = 'Данные взяты с сайта allworld.xyz и' \
                              ' предназначены только для его посетителей.'
    return JsonResponse(content)
