# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text
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
            weather_server = 'api.wunderground.com'
            weather_page = '/api/d3de2d8a8d6e227e/geolookup/conditions/' \
                           'forecast/lang:RU/q/Russia/Saint%20Petersburg.json'
            conn = http.client.HTTPSConnection(weather_server, timeout=25)
            conn.request("GET", weather_page)
            obj_conn = conn.getresponse()
            text = obj_conn.read()
            conn.close()
        except Exception as err:
            text = 'Получить погоду не удалось: '  # + err

        context = super().get_context_data(**kwargs)
        context['weather_text'] = 'Тут будет реальная погода!!! - '\
                                  + str(text)
        return context
