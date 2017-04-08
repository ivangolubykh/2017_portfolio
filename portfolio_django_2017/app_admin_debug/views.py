# from django.shortcuts import render
from django.views.generic.list import ListView
from app_main.models import MainHeader1Text, MainHeader2Text, MainHeader3Text,\
    MainHeader4Text, MainText


# Главная страница админки:
class AdminListView(ListView):
    queryset = MainHeader1Text.objects.order_by('ordinal'). \
        prefetch_related('mainheader2text_set',
                         'mainheader2text_set__mainheader3text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set',
                         'mainheader2text_set__mainheader3text_set__'
                         'mainheader4text_set__maintext_set')
    template_name = 'admin.html'
