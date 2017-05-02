"""django_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import AdminListView, H1Create, H2Create, H3Create, H4Create, \
    TextCreate, H1Delete, H2Delete, H3Delete, H4Delete, TextDelete, H1Update,\
    H2Update, H3Update, H4Update, TextUpdate, AdminExamplesPythonListView,\
    AdminExamplesPythonH1Create, AdminExamplesPythonH2Create,\
    AdminExamplesPythonH3Create, AdminExamplesPythonH4Create,\
    AdminExamplesPythonTextCreate, AdminExamplesPythonH1Delete,\
    AdminExamplesPythonH2Delete, AdminExamplesPythonH3Delete,\
    AdminExamplesPythonH4Delete, AdminExamplesPythonTextDelete,\
    AdminExamplesPythonH1Update, AdminExamplesPythonH2Update,\
    AdminExamplesPythonH3Update, AdminExamplesPythonH4Update,\
    AdminExamplesPythonTextUpdate


# Блок страниц админки для главной страницы:
urlpatterns = [
    url(r'^admin/$', AdminListView.as_view(), name='admin'),
    url(r'admin/add_main_h1/$', H1Create.as_view(), name='admin_main-add_h1'),
    url(r'admin/add_main_h2/$', H2Create.as_view(), name='admin_main-add_h2'),
    url(r'admin/add_main_h3/$', H3Create.as_view(), name='admin_main-add_h3'),
    url(r'admin/add_main_h4/$', H4Create.as_view(), name='admin_main-add_h4'),
    url(r'admin/add_main_text/$', TextCreate.as_view(),
        name='admin_main-add_text'),
    url(r'admin/del_main_h1/(?P<pk>[\w]+)/$', H1Delete.as_view(),
        name='admin_main-del_h1'),
    url(r'admin/del_main_h2/(?P<pk>[\w]+)/$', H2Delete.as_view(),
        name='admin_main-del_h2'),
    url(r'admin/del_main_h3/(?P<pk>[\w]+)/$', H3Delete.as_view(),
        name='admin_main-del_h3'),
    url(r'admin/del_main_h4/(?P<pk>[\w]+)/$', H4Delete.as_view(),
        name='admin_main-del_h4'),
    url(r'admin/del_main_text/(?P<pk>[\w]+)/$', TextDelete.as_view(),
        name='admin_main-del_text'),
    url(r'admin/update_main_h1/(?P<pk>[\w]+)/$', H1Update.as_view(),
        name='admin_main-update_h1'),
    url(r'admin/update_main_h2/(?P<pk>[\w]+)/$', H2Update.as_view(),
        name='admin_main-update_h2'),
    url(r'admin/update_main_h3/(?P<pk>[\w]+)/$', H3Update.as_view(),
        name='admin_main-update_h3'),
    url(r'admin/update_main_h4/(?P<pk>[\w]+)/$', H4Update.as_view(),
        name='admin_main-update_h4'),
    url(r'admin/update_main_text/(?P<pk>[\w]+)/$', TextUpdate.as_view(),
        name='admin_main-update_text'),
]

# Блок страниц админки для страницы примеров работ:
urlpatterns += [
    url(r'^admin_examples_work_python/$',
        AdminExamplesPythonListView.as_view(),
        name='admin_examples_work_python'),
    url(r'admin_examples_work_python/add_main_h1/$',
        AdminExamplesPythonH1Create.as_view(),
        name='admin_examples_work_python-add_h1'),
    url(r'admin_examples_work_python/add_main_h2/$',
        AdminExamplesPythonH2Create.as_view(),
        name='admin_examples_work_python-add_h2'),
    url(r'admin_examples_work_python/add_main_h3/$',
        AdminExamplesPythonH3Create.as_view(),
        name='admin_examples_work_python-add_h3'),
    url(r'admin_examples_work_python/add_main_h4/$',
        AdminExamplesPythonH4Create.as_view(),
        name='admin_examples_work_python-add_h4'),
    url(r'admin_examples_work_python/add_main_text/$',
        AdminExamplesPythonTextCreate.as_view(),
        name='admin_examples_work_python-add_text'),
    url(r'admin_examples_work_python/del_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH1Delete.as_view(),
        name='admin_examples_work_python-del_h1'),
    url(r'admin_examples_work_python/del_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH2Delete.as_view(),
        name='admin_examples_work_python-del_h2'),
    url(r'admin_examples_work_python/del_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH3Delete.as_view(),
        name='admin_examples_work_python-del_h3'),
    url(r'admin_examples_work_python/del_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH4Delete.as_view(),
        name='admin_examples_work_python-del_h4'),
    url(r'admin_examples_work_python/del_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesPythonTextDelete.as_view(),
        name='admin_examples_work_python-del_text'),
    url(r'admin_examples_work_python/update_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH1Update.as_view(),
        name='admin_examples_work_python-update_h1'),
    url(r'admin_examples_work_python/update_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH2Update.as_view(),
        name='admin_examples_work_python-update_h2'),
    url(r'admin_examples_work_python/update_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH3Update.as_view(),
        name='admin_examples_work_python-update_h3'),
    url(r'admin_examples_work_python/update_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH4Update.as_view(),
        name='admin_examples_work_python-update_h4'),
    url(r'admin_examples_work_python/update_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesPythonTextUpdate.as_view(),
        name='admin_examples_work_python-update_text'),
]
