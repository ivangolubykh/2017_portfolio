# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models_examples_work_python import \
    ExamplesPythonHeaderorList1Text, ExamplesPythonHeaderorList2Text,\
    ExamplesPythonHeaderorList3Text, ExamplesPythonHeaderorList4Text,\
    ExamplesPythonText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesPythonListView(ListView):
    queryset = ExamplesPythonHeaderorList1Text.objects.order_by('ordinal'). \
        prefetch_related('examplespythonheaderorlist2text_set',
                         'examplespythonheaderorlist2text__examplespythonheaderorlist3text_set',
                         'examplespythonheaderorlist2text_set__examplespythonheaderorlist3text_set__'
                         'examplespythonheaderorlist4text_set',
                         'examplespythonheaderorlist2text_set__examplespythonheaderorlist3text_set__'
                         'examplespythonheaderorlist4text_set__examplespythontext_set')
    template_name = 'admin_examples_python.html'


class AdminExamplesPythonH1Create(CreateView):
    model = ExamplesPythonHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonH2Create(CreateView):
    model = ExamplesPythonHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonH3Create(CreateView):
    model = ExamplesPythonHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonH4Create(CreateView):
    model = ExamplesPythonHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonTextCreate(CreateView):
    model = ExamplesPythonText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesPythonH1Delete(DeleteView):
    model = ExamplesPythonHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonH2Delete(DeleteView):
    model = ExamplesPythonHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonH3Delete(DeleteView):
    model = ExamplesPythonHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonH4Delete(DeleteView):
    model = ExamplesPythonHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonTextDelete(DeleteView):
    model = ExamplesPythonText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesPythonH1Update(UpdateView):
    model = ExamplesPythonHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminExamplesPythonH2Update(UpdateView):
    model = ExamplesPythonHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesPythonH3Update(UpdateView):
    model = ExamplesPythonHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesPythonH4Update(UpdateView):
    model = ExamplesPythonHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesPythonTextUpdate(UpdateView):
    model = ExamplesPythonText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
