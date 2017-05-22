# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import ExamplesJs
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesJsListView(ListView):
    queryset = ExamplesJs.objects.order_by('ordinal').reverse()
    template_name = 'admin_examples_work_js.html'


class AdminExamplesJsCreate(CreateView):
    model = ExamplesJs
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesJsDelete(DeleteView):
    model = ExamplesJs
    success_url = reverse_lazy('admin_examples_work_js')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsUpdate(UpdateView):
    model = ExamplesJs
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_update.html'
