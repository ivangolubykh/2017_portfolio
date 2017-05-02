# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import \
    ExamplesHtmlCssHeaderorList1Text, ExamplesHtmlCssHeaderorList2Text,\
    ExamplesHtmlCssHeaderorList3Text, ExamplesHtmlCssHeaderorList4Text,\
    ExamplesHtmlCssText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesHtmlCssListView(ListView):
    queryset = ExamplesHtmlCssHeaderorList1Text.objects.order_by('ordinal'). \
        prefetch_related('exampleshtmlcssheaderorlist2text_set',
                         'exampleshtmlcssheaderorlist2text_set__'
                         'exampleshtmlcssheaderorlist3text_set',
                         'exampleshtmlcssheaderorlist2text_set__'
                         'exampleshtmlcssheaderorlist3text_set__'
                         'exampleshtmlcssheaderorlist4text_set',
                         'exampleshtmlcssheaderorlist2text_set__'
                         'exampleshtmlcssheaderorlist3text_set__'
                         'exampleshtmlcssheaderorlist4text_set__'
                         'exampleshtmlcsstext_set')
    template_name = 'admin_examples_work_html_css.html'


class AdminExamplesHtmlCssH1Create(CreateView):
    model = ExamplesHtmlCssHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssH2Create(CreateView):
    model = ExamplesHtmlCssHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssH3Create(CreateView):
    model = ExamplesHtmlCssHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssH4Create(CreateView):
    model = ExamplesHtmlCssHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssTextCreate(CreateView):
    model = ExamplesHtmlCssText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesHtmlCssH1Delete(DeleteView):
    model = ExamplesHtmlCssHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssH2Delete(DeleteView):
    model = ExamplesHtmlCssHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssH3Delete(DeleteView):
    model = ExamplesHtmlCssHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssH4Delete(DeleteView):
    model = ExamplesHtmlCssHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssTextDelete(DeleteView):
    model = ExamplesHtmlCssText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesHtmlCssH1Update(UpdateView):
    model = ExamplesHtmlCssHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminExamplesHtmlCssH2Update(UpdateView):
    model = ExamplesHtmlCssHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesHtmlCssH3Update(UpdateView):
    model = ExamplesHtmlCssHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesHtmlCssH4Update(UpdateView):
    model = ExamplesHtmlCssHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesHtmlCssTextUpdate(UpdateView):
    model = ExamplesHtmlCssText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
