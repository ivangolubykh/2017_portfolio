# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text


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
        context['weather_text'] = 'Тут будет реальная погода!!!'
        return context