# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text
import requests


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
        try:
            url = 'http://api.wunderground.com//api/d3de2d8a8d6e227e/' \
                  'geolookup/conditions/forecast/lang:RU/q/Russia/' \
                  'Saint Petersburg.json'
            response = requests.get(url)
            image = response.json()["current_observation"]["icon_url"]
            temperature = response.json()["current_observation"]["temp_c"]
            text = response.json()["current_observation"]["weather"]
        except Exception as err:
            text = 'Получить погоду не удалось: ' + err

        context = super().get_context_data(**kwargs)
        context['weather_image'] = image
        context['weather_temperature'] = temperature
        context['weather_text'] = text
        return context
