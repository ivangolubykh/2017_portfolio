# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import Works
from django.core.urlresolvers import reverse_lazy

__author__ = 'Иван Голубых'


# Пдминка текстов для страницы примеров работ на питоне:
class AdminWorksListView(ListView):
    queryset = Works.objects.order_by('ordinal').reverse()
    template_name = 'admin_works.html'


class AdminWorksCreate(CreateView):
    model = Works
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminWorksDelete(DeleteView):
    model = Works
    success_url = reverse_lazy('admin_works')
    template_name = 'admin_main_delete.html'


class AdminWorksUpdate(UpdateView):
    model = Works
    fields = ['ordinal', 'text']
    template_name = 'admin_main_update.html'
