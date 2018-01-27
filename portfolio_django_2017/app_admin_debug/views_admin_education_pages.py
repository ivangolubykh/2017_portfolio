# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import Education
from django.core.urlresolvers import reverse_lazy

__author__ = 'Иван Голубых'


# Пдминка текстов для страницы примеров работ на питоне:
class AdminEducationListView(ListView):
    queryset = Education.objects.order_by('ordinal').reverse()
    template_name = 'admin_education.html'


class AdminEducationCreate(CreateView):
    model = Education
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminEducationDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('admin_education')
    template_name = 'admin_main_delete.html'


class AdminEducationUpdate(UpdateView):
    model = Education
    fields = ['ordinal', 'text']
    template_name = 'admin_main_update.html'
