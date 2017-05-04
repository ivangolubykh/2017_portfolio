# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text, Weather_For_Json
import requests
from django.http import JsonResponse
from portfolio_django_2017.settings import STATIC_URL
from django.db import transaction
from django.utils import timezone
from django.core.urlresolvers import reverse


def crumbs(object):
    ''' Функция генерации хлебных крошек. Для её работы необходимо в каждой
    функции/классе иметь 3 переменных:
        crumbs_page_name = < Текстовое название ссылки на эту страницу >
        crumbs_page_urlname = < Имя страницы в UrlConf (для reverse) >
        crumbs_up = < Ссылка на функцию/класс родительской страницы >
    Для запуска функции в качестве параметра object надо передать ссылку на
    текущую функцию или класс, из которой вызваны хлебные крошки, например:
     crumbs(__class__)
    '''
    html_str = ''
    if object.crumbs_up:
        html_str += crumbs(object.crumbs_up) + ' &rarr; '
    html_str += '<a href="{}">{}</a>'.\
        format(reverse(object.crumbs_page_urlname), object.crumbs_page_name)
    return html_str


# Главная страница:
class MainListView(ListView):
    # model = MainText
    crumbs_page_name = 'Главная'
    crumbs_page_urlname = 'main'
    crumbs_up = False
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
        if 'session_exist' not in self.request.session or\
                not self.request.session['session_exist']:
            self.request.session['session_exist'] = True
        return context


# Генерация Json с погодой для аякса на главной странице.
def weather_json(request):
    # Буду обновлять БД не чаще 1 раза в 15 минут (900 секунд):
    TIME_DELTA_TO_UPDATE_WEATHER = 900
    content = {}
    if 'session_exist' in request.session and request.session['session_exist']:
        with transaction.atomic():
            # Начинаю транзакцию для избежания одновременного запроса данных
            # погоды несколькими посетителями:
            try:
                weather = Weather_For_Json.objects.get(pk=1)
            except Weather_For_Json.DoesNotExist:
                weather = Weather_For_Json(pk=1, image='', temperature='',
                                           text='')
                weather.save()

            old_time = weather.datetime + timezone.timedelta(
                seconds=TIME_DELTA_TO_UPDATE_WEATHER)
            current_time = timezone.now()
            if old_time < current_time:
                # Пора обновить данные в БД
                try:
                    url = 'http://api.wunderground.com//api/' \
                          'd3de2d8a8d6e227e/geolookup/conditions/forecast/' \
                          'lang:RU/q/Russia/Saint Petersburg.json'
                    response = requests.get(url)
                    image = response.json()["current_observation"]["icon_url"]
                    image = image.replace('http://', 'https://')
                    temperature = response. \
                        json()["current_observation"]["temp_c"]
                    text = response.json()["current_observation"]["weather"]
                    weather = Weather_For_Json(pk=1, image=image,
                                               temperature=temperature,
                                               text=text)
                    weather.save()
                    content['weather_image'] = image
                    content['weather_temperature'] = temperature
                    content['weather_text'] = text
                except Exception as err:
                    content['weather_image'] = STATIC_URL +\
                                               'general/img/empty.gif'
                    content['weather_temperature'] = ''
                    content['weather_text'] = 'Получить погоду' \
                                              ' не удалось: '  # + err
            else:
                # Беру старые данные из БД
                weather = Weather_For_Json.objects.get(pk=1)
                content['weather_image'] = weather.image
                content['weather_temperature'] = weather.temperature
                content['weather_text'] = weather.text
        return JsonResponse(content)
    content['weather_image'] = ''
    content['weather_temperature'] = ''
    content['weather_text'] = 'Данные взяты с сайта allworld.xyz и' \
                              ' предназначены только для его посетителей.'
    return JsonResponse(content)


# Страница Примеры Работ:
class ExamplesWorkListView(ListView):
    crumbs_page_name = 'Примеры работ'
    crumbs_page_urlname = 'examples_work'
    crumbs_up = MainListView
    # model = MainText
    queryset = MainHeader1Text.objects.order_by('ordinal').\
        prefetch_related('mainheader2text_set',
                         'mainheader2text_set__mainheader3text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set__maintext_set')
    template_name = 'examples_work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # создаю сессию для подрузки данных Ajax-ом только для своих
        # посетителей:
        if 'session_exist' not in self.request.session or\
                not self.request.session['session_exist']:
            self.request.session['session_exist'] = True
        context['crumbs'] = crumbs(__class__)
        return context
