# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import MainHeader1Text, MainHeader2Text, MainHeader3Text,\
    MainHeader4Text, MainText
from django.core.urlresolvers import reverse_lazy


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


class H1Create(CreateView):
    model = MainHeader1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_create.html'
    succes_url = reverse_lazy('admin')


class H2Create(CreateView):
    model = MainHeader2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_create.html'
    succes_url = reverse_lazy('admin')


class H3Create(CreateView):
    model = MainHeader3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_create.html'
    succes_url = reverse_lazy('admin')


class H4Create(CreateView):
    model = MainHeader4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_create.html'
    succes_url = reverse_lazy('admin')


class TextCreate(CreateView):
    model = MainText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_create.html'
    succes_url = reverse_lazy('admin')
