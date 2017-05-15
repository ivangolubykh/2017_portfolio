# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import ExamplesPython
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesPythonListView(ListView):
    queryset = ExamplesPython.objects.order_by('ordinal')
    template_name = 'admin_examples_work_python.html'


class AdminExamplesPythonH1Create(CreateView):
    model = ExamplesPython
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonH1Delete(DeleteView):
    model = ExamplesPython
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonH1Update(UpdateView):
    model = ExamplesPython
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']
