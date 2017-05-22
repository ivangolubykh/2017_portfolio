# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import ExamplesHtmlCss
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesHtmlCssListView(ListView):
    queryset = ExamplesHtmlCss.objects.order_by('ordinal').reverse()
    template_name = 'admin_examples_work_html_css.html'


class AdminExamplesHtmlCssCreate(CreateView):
    model = ExamplesHtmlCss
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssDelete(DeleteView):
    model = ExamplesHtmlCss
    success_url = reverse_lazy('admin_examples_work_html_css')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssUpdate(UpdateView):
    model = ExamplesHtmlCss
    fields = ['ordinal', 'name_project', 'image_file', 'net_address',
              'git_address', 'text']
    template_name = 'admin_main_update.html'
