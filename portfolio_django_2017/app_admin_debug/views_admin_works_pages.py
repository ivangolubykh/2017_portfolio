# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_main.models import \
    WorksHeaderorList1Text, WorksHeaderorList2Text,\
    WorksHeaderorList3Text, WorksHeaderorList4Text,\
    WorksText
from django.core.urlresolvers import reverse_lazy


# Пдминка текстов для страницы примеров работ на Учёбы:
class AdminWorksListView(ListView):
    queryset = WorksHeaderorList1Text.objects.order_by('ordinal').\
        prefetch_related('worksheaderorlist2text_set',
                         'worksheaderorlist2text_set__'
                         'worksheaderorlist3text_set',
                         'worksheaderorlist2text_set__'
                         'worksheaderorlist3text_set__'
                         'worksheaderorlist4text_set',
                         'worksheaderorlist2text_set__'
                         'worksheaderorlist3text_set__'
                         'worksheaderorlist4text_set__'
                         'workstext_set')
    template_name = 'admin_works.html'


class AdminWorksH1Create(CreateView):
    model = WorksHeaderorList1Text
    fields = ['ordinal', 'text']
    template_name = 'admin_main_create.html'


class AdminWorksH2Create(CreateView):
    model = WorksHeaderorList2Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminWorksH3Create(CreateView):
    model = WorksHeaderorList3Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminWorksH4Create(CreateView):
    model = WorksHeaderorList4Text
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminWorksTextCreate(CreateView):
    model = WorksText
    fields = ['ordinal', 'text', 'up']
    template_name = 'admin_main_create.html'


class AdminWorksH1Delete(DeleteView):
    model = WorksHeaderorList1Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminWorksH2Delete(DeleteView):
    model = WorksHeaderorList2Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminWorksH3Delete(DeleteView):
    model = WorksHeaderorList3Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminWorksH4Delete(DeleteView):
    model = WorksHeaderorList4Text
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminWorksTextDelete(DeleteView):
    model = WorksText
    success_url = reverse_lazy('admin')
    template_name = 'admin_main_delete.html'


class AdminWorksH1Update(UpdateView):
    model = WorksHeaderorList1Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text']


class AdminWorksH2Update(UpdateView):
    model = WorksHeaderorList2Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminWorksH3Update(UpdateView):
    model = WorksHeaderorList3Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminWorksH4Update(UpdateView):
    model = WorksHeaderorList4Text
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']


class AdminWorksTextUpdate(UpdateView):
    model = WorksText
    template_name = 'admin_main_update.html'
    fields = ['ordinal', 'text', 'up']
