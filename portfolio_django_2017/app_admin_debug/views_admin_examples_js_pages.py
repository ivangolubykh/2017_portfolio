# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import \
    ExamplesJsHeaderorList1Text, ExamplesJsHeaderorList2Text,\
    ExamplesJsHeaderorList3Text, ExamplesJsHeaderorList4Text,\
    ExamplesJsText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на питоне:
class AdminExamplesJsListView(ListView):
    queryset = ExamplesJsHeaderorList1Text.objects.order_by('ordinal'). \
        prefetch_related('examplesjsheaderorlist2text_set',
                         'examplesjsheaderorlist2text_set__'
                         'examplesjsheaderorlist3text_set',
                         'examplesjsheaderorlist2text_set__'
                         'examplesjsheaderorlist3text_set__'
                         'examplesjsheaderorlist4text_set',
                         'examplesjsheaderorlist2text_set__'
                         'examplesjsheaderorlist3text_set__'
                         'examplesjsheaderorlist4text_set__'
                         'examplesjstext_set')
    template_name = 'admin_examples_work_js.html'


class AdminExamplesJsH1Create(CreateView):
    model = ExamplesJsHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesJsH2Create(CreateView):
    model = ExamplesJsHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesJsH3Create(CreateView):
    model = ExamplesJsHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesJsH4Create(CreateView):
    model = ExamplesJsHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesJsTextCreate(CreateView):
    model = ExamplesJsText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesJsH1Delete(DeleteView):
    model = ExamplesJsHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsH2Delete(DeleteView):
    model = ExamplesJsHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsH3Delete(DeleteView):
    model = ExamplesJsHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsH4Delete(DeleteView):
    model = ExamplesJsHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsTextDelete(DeleteView):
    model = ExamplesJsText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesJsH1Update(UpdateView):
    model = ExamplesJsHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminExamplesJsH2Update(UpdateView):
    model = ExamplesJsHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesJsH3Update(UpdateView):
    model = ExamplesJsHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesJsH4Update(UpdateView):
    model = ExamplesJsHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesJsTextUpdate(UpdateView):
    model = ExamplesJsText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
