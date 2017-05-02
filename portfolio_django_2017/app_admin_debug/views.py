# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import MainHeader1Text, MainHeader2Text, MainHeader3Text,\
    MainHeader4Text, MainText
from django.core.urlresolvers import reverse_lazy

# Для удобства восприятия и обслуживания вынес блоки по разным файлам, а то
# очень трудно в ворохе схожего найти нужное.
from .views_admin_main_pages import *
from .views_admin_examples_python_pages import *
from .views_admin_examples_js_pages import *
from .views_admin_examples_html_css_pages import *