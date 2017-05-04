# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import \
    EducationHeaderorList1Text, EducationHeaderorList2Text,\
    EducationHeaderorList3Text, EducationHeaderorList4Text,\
    EducationText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на Учёбы:
class AdminEducationListView(ListView):
    queryset = EducationHeaderorList1Text.objects.order_by('ordinal').\
        prefetch_related('educationheaderorlist2text_set',
                         'educationheaderorlist2text_set__'
                         'educationheaderorlist3text_set',
                         'educationheaderorlist2text_set__'
                         'educationheaderorlist3text_set__'
                         'educationheaderorlist4text_set',
                         'educationheaderorlist2text_set__'
                         'educationheaderorlist3text_set__'
                         'educationheaderorlist4text_set__'
                         'educationtext_set')
    template_name = 'admin_education.html'


class AdminEducationH1Create(CreateView):
    model = EducationHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminEducationH2Create(CreateView):
    model = EducationHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminEducationH3Create(CreateView):
    model = EducationHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminEducationH4Create(CreateView):
    model = EducationHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminEducationTextCreate(CreateView):
    model = EducationText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminEducationH1Delete(DeleteView):
    model = EducationHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminEducationH2Delete(DeleteView):
    model = EducationHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminEducationH3Delete(DeleteView):
    model = EducationHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminEducationH4Delete(DeleteView):
    model = EducationHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminEducationTextDelete(DeleteView):
    model = EducationText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminEducationH1Update(UpdateView):
    model = EducationHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminEducationH2Update(UpdateView):
    model = EducationHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminEducationH3Update(UpdateView):
    model = EducationHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminEducationH4Update(UpdateView):
    model = EducationHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminEducationTextUpdate(UpdateView):
    model = EducationText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
