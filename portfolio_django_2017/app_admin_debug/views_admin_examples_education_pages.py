# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import \
    ExamplesEducationHeaderorList1Text, ExamplesEducationHeaderorList2Text,\
    ExamplesEducationHeaderorList3Text, ExamplesEducationHeaderorList4Text,\
    ExamplesEducationText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на Учёбы:
class AdminExamplesEducationListView(ListView):
    queryset = ExamplesEducationHeaderorList1Text.objects.order_by('ordinal').\
        prefetch_related('exampleseducationheaderorlist2text_set',
                         'exampleseducationheaderorlist2text_set__'
                         'exampleseducationheaderorlist3text_set',
                         'exampleseducationheaderorlist2text_set__'
                         'exampleseducationheaderorlist3text_set__'
                         'exampleseducationheaderorlist4text_set',
                         'exampleseducationheaderorlist2text_set__'
                         'exampleseducationheaderorlist3text_set__'
                         'exampleseducationheaderorlist4text_set__'
                         'exampleseducationtext_set')
    template_name = 'admin_examples_work_education.html'


class AdminExamplesEducationH1Create(CreateView):
    model = ExamplesEducationHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminExamplesEducationH2Create(CreateView):
    model = ExamplesEducationHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesEducationH3Create(CreateView):
    model = ExamplesEducationHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesEducationH4Create(CreateView):
    model = ExamplesEducationHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesEducationTextCreate(CreateView):
    model = ExamplesEducationText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminExamplesEducationH1Delete(DeleteView):
    model = ExamplesEducationHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesEducationH2Delete(DeleteView):
    model = ExamplesEducationHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesEducationH3Delete(DeleteView):
    model = ExamplesEducationHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesEducationH4Delete(DeleteView):
    model = ExamplesEducationHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesEducationTextDelete(DeleteView):
    model = ExamplesEducationText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminExamplesEducationH1Update(UpdateView):
    model = ExamplesEducationHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminExamplesEducationH2Update(UpdateView):
    model = ExamplesEducationHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesEducationH3Update(UpdateView):
    model = ExamplesEducationHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesEducationH4Update(UpdateView):
    model = ExamplesEducationHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminExamplesEducationTextUpdate(UpdateView):
    model = ExamplesEducationText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
