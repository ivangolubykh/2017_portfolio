# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import ExamplesPython
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesPythonListView(ListView):
    queryset = ExamplesPython.objects.order_by('ordinal').reverse()
    template_name = 'admin_examples_work_python.html'


class AdminExamplesPythonCreate(CreateView):
    model = ExamplesPython
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonDelete(DeleteView):
    model = ExamplesPython
    success_url = reverse_lazy('admin_examples_work_python')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonUpdate(UpdateView):
    model = ExamplesPython
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_update.html'
