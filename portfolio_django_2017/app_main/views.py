# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text
import requests
import http.client


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
            text = response.json()["response"]["version"]
        except Exception as err:
            text = 'Получить погоду не удалось: '  # + err

        context = super().get_context_data(**kwargs)
        context['weather_text'] = 'Тут будет реальная погода!!! - '\
                                  + text
        return context
