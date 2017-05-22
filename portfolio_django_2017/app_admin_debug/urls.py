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
    H2Update, H3Update, H4Update, TextUpdate,\
    AdminExamplesPythonListView, AdminExamplesPythonCreate,\
    AdminExamplesPythonDelete, AdminExamplesPythonUpdate,\
    AdminExamplesJsListView, AdminExamplesJsCreate, AdminExamplesJsDelete, \
    AdminExamplesJsUpdate,\
    AdminExamplesHtmlCssListView, AdminExamplesHtmlCssCreate,\
    AdminExamplesHtmlCssDelete, AdminExamplesHtmlCssUpdate,\
    AdminEducationListView, AdminEducationCreate, AdminEducationDelete, \
    AdminEducationUpdate,\
    AdminWorksListView, AdminWorksCreate, AdminWorksDelete, AdminWorksUpdate

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

# Блок страниц админки для страницы примеров работ на питоне:
urlpatterns += [
    url(r'^admin_examples_work_python/$',
        AdminExamplesPythonListView.as_view(),
        name='admin_examples_work_python'),
    url(r'admin_examples_work_python/add/$',
        AdminExamplesPythonCreate.as_view(),
        name='admin_examples_work_python-add'),
    url(r'admin_examples_work_python/del/(?P<pk>[\w]+)/$',
        AdminExamplesPythonDelete.as_view(),
        name='admin_examples_work_python-del'),
    url(r'admin_examples_work_python/update/(?P<pk>[\w]+)/$',
        AdminExamplesPythonUpdate.as_view(),
        name='admin_examples_work_python-update'),
]

# Блок страниц админки для страницы примеров работ на JavaScript:
urlpatterns += [
    url(r'^admin_examples_work_js/$',
        AdminExamplesJsListView.as_view(),
        name='admin_examples_work_js'),
    url(r'admin_examples_work_js/add/$',
        AdminExamplesJsCreate.as_view(),
        name='admin_examples_work_js-add'),
    url(r'admin_examples_work_js/del/(?P<pk>[\w]+)/$',
        AdminExamplesJsDelete.as_view(),
        name='admin_examples_work_js-del'),
    url(r'admin_examples_work_js/update/(?P<pk>[\w]+)/$',
        AdminExamplesJsUpdate.as_view(),
        name='admin_examples_work_js-update'),
]

# Блок страниц админки для страницы примеров работ на Html5/Css:
urlpatterns += [
    url(r'^admin_examples_work_html_css/$',
        AdminExamplesHtmlCssListView.as_view(),
        name='admin_examples_work_html_css'),
    url(r'admin_examples_work_html_css/add/$',
        AdminExamplesHtmlCssCreate.as_view(),
        name='admin_examples_work_html_css-add'),
    url(r'admin_examples_work_html_css/del/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssDelete.as_view(),
        name='admin_examples_work_html_css-del'),
    url(r'admin_examples_work_html_css/update/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssUpdate.as_view(),
        name='admin_examples_work_html_css-update'),
]

# Блок страниц админки для страницы Учёбы:
urlpatterns += [
    url(r'^admin_education/$',
        AdminEducationListView.as_view(),
        name='admin_education'),
    url(r'admin_education/add/$',
        AdminEducationCreate.as_view(),
        name='admin_education-add'),
    url(r'admin_education/del/(?P<pk>[\w]+)/$',
        AdminEducationDelete.as_view(),
        name='admin_education-del'),
    url(r'admin_education/update/(?P<pk>[\w]+)/$',
        AdminEducationUpdate.as_view(),
        name='admin_education-update'),
]

# Блок страниц админки для страницы Работы:
urlpatterns += [
    url(r'^admin_works/$',
        AdminWorksListView.as_view(),
        name='admin_works'),
    url(r'admin_works/add/$',
        AdminWorksCreate.as_view(),
        name='admin_works-add'),
    url(r'admin_works/del/(?P<pk>[\w]+)/$',
        AdminWorksDelete.as_view(),
        name='admin_works-del'),
    url(r'admin_works/update/(?P<pk>[\w]+)/$',
        AdminWorksUpdate.as_view(),
        name='admin_works-update'),
]
