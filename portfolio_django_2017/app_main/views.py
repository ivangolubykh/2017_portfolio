# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import MainHeader1Text, MainHeader2Text, MainHeader3Text,\
    MainHeader4Text, MainText


# Главная страница:
class MainListView(ListView):
    # model = MainText
    queryset = MainHeader1Text.objects.order_by('ordinal').\
        prefetch_related('mainheader2text_set',
                         'mainheader2text_set.mainheader3text_set',
                         'mainheader2text_set.mainheader3text_set.'
                         'mainheader4text_set',
                         'mainheader2text_set.mainheader3text_set.'
                         'mainheader4text_set.maintext_set')
    template_name = 'index.html'
