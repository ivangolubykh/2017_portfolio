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
    AdminExamplesPythonListView,\
    AdminExamplesPythonH1Create, AdminExamplesPythonH1Delete,\
    AdminExamplesPythonH1Update,\
    AdminExamplesJsListView, \
    AdminExamplesJsH1Create, AdminExamplesJsH2Create, \
    AdminExamplesJsH3Create, AdminExamplesJsH4Create, \
    AdminExamplesJsTextCreate, AdminExamplesJsH1Delete, \
    AdminExamplesJsH2Delete, AdminExamplesJsH3Delete, \
    AdminExamplesJsH4Delete, AdminExamplesJsTextDelete, \
    AdminExamplesJsH1Update, AdminExamplesJsH2Update, \
    AdminExamplesJsH3Update, AdminExamplesJsH4Update, \
    AdminExamplesJsTextUpdate,\
    AdminExamplesHtmlCssListView, \
    AdminExamplesHtmlCssH1Create, AdminExamplesHtmlCssH2Create, \
    AdminExamplesHtmlCssH3Create, AdminExamplesHtmlCssH4Create, \
    AdminExamplesHtmlCssTextCreate, AdminExamplesHtmlCssH1Delete, \
    AdminExamplesHtmlCssH2Delete, AdminExamplesHtmlCssH3Delete, \
    AdminExamplesHtmlCssH4Delete, AdminExamplesHtmlCssTextDelete, \
    AdminExamplesHtmlCssH1Update, AdminExamplesHtmlCssH2Update, \
    AdminExamplesHtmlCssH3Update, AdminExamplesHtmlCssH4Update, \
    AdminExamplesHtmlCssTextUpdate,\
    AdminEducationListView, \
    AdminEducationH1Create, AdminEducationH2Create, \
    AdminEducationH3Create, AdminEducationH4Create, \
    AdminEducationTextCreate, AdminEducationH1Delete, \
    AdminEducationH2Delete, AdminEducationH3Delete, \
    AdminEducationH4Delete, AdminEducationTextDelete, \
    AdminEducationH1Update, AdminEducationH2Update, \
    AdminEducationH3Update, AdminEducationH4Update, \
    AdminEducationTextUpdate,\
    AdminWorksListView, \
    AdminWorksH1Create, AdminWorksH2Create, \
    AdminWorksH3Create, AdminWorksH4Create, \
    AdminWorksTextCreate, AdminWorksH1Delete, \
    AdminWorksH2Delete, AdminWorksH3Delete, \
    AdminWorksH4Delete, AdminWorksTextDelete, \
    AdminWorksH1Update, AdminWorksH2Update, \
    AdminWorksH3Update, AdminWorksH4Update, \
    AdminWorksTextUpdate

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
    url(r'admin_examples_work_python/add_main_h1/$',
        AdminExamplesPythonH1Create.as_view(),
        name='admin_examples_work_python-add_h1'),
    url(r'admin_examples_work_python/del_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH1Delete.as_view(),
        name='admin_examples_work_python-del_h1'),
    url(r'admin_examples_work_python/update_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesPythonH1Update.as_view(),
        name='admin_examples_work_python-update_h1'),
]

# Блок страниц админки для страницы примеров работ на JavaScript:
urlpatterns += [
    url(r'^admin_examples_work_js/$',
        AdminExamplesJsListView.as_view(),
        name='admin_examples_work_js'),
    url(r'admin_examples_work_js/add_main_h1/$',
        AdminExamplesJsH1Create.as_view(),
        name='admin_examples_work_js-add_h1'),
    url(r'admin_examples_work_js/add_main_h2/$',
        AdminExamplesJsH2Create.as_view(),
        name='admin_examples_work_js-add_h2'),
    url(r'admin_examples_work_js/add_main_h3/$',
        AdminExamplesJsH3Create.as_view(),
        name='admin_examples_work_js-add_h3'),
    url(r'admin_examples_work_js/add_main_h4/$',
        AdminExamplesJsH4Create.as_view(),
        name='admin_examples_work_js-add_h4'),
    url(r'admin_examples_work_js/add_main_text/$',
        AdminExamplesJsTextCreate.as_view(),
        name='admin_examples_work_js-add_text'),
    url(r'admin_examples_work_js/del_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesJsH1Delete.as_view(),
        name='admin_examples_work_js-del_h1'),
    url(r'admin_examples_work_js/del_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesJsH2Delete.as_view(),
        name='admin_examples_work_js-del_h2'),
    url(r'admin_examples_work_js/del_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesJsH3Delete.as_view(),
        name='admin_examples_work_js-del_h3'),
    url(r'admin_examples_work_js/del_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesJsH4Delete.as_view(),
        name='admin_examples_work_js-del_h4'),
    url(r'admin_examples_work_js/del_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesJsTextDelete.as_view(),
        name='admin_examples_work_js-del_text'),
    url(r'admin_examples_work_js/update_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesJsH1Update.as_view(),
        name='admin_examples_work_js-update_h1'),
    url(r'admin_examples_work_js/update_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesJsH2Update.as_view(),
        name='admin_examples_work_js-update_h2'),
    url(r'admin_examples_work_js/update_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesJsH3Update.as_view(),
        name='admin_examples_work_js-update_h3'),
    url(r'admin_examples_work_js/update_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesJsH4Update.as_view(),
        name='admin_examples_work_js-update_h4'),
    url(r'admin_examples_work_js/update_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesJsTextUpdate.as_view(),
        name='admin_examples_work_js-update_text'),
]

# Блок страниц админки для страницы примеров работ на Html5/Css:
urlpatterns += [
    url(r'^admin_examples_work_html_css/$',
        AdminExamplesHtmlCssListView.as_view(),
        name='admin_examples_work_html_css'),
    url(r'admin_examples_work_html_css/add_main_h1/$',
        AdminExamplesHtmlCssH1Create.as_view(),
        name='admin_examples_work_html_css-add_h1'),
    url(r'admin_examples_work_html_css/add_main_h2/$',
        AdminExamplesHtmlCssH2Create.as_view(),
        name='admin_examples_work_html_css-add_h2'),
    url(r'admin_examples_work_html_css/add_main_h3/$',
        AdminExamplesHtmlCssH3Create.as_view(),
        name='admin_examples_work_html_css-add_h3'),
    url(r'admin_examples_work_html_css/add_main_h4/$',
        AdminExamplesHtmlCssH4Create.as_view(),
        name='admin_examples_work_html_css-add_h4'),
    url(r'admin_examples_work_html_css/add_main_text/$',
        AdminExamplesHtmlCssTextCreate.as_view(),
        name='admin_examples_work_html_css-add_text'),
    url(r'admin_examples_work_html_css/del_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH1Delete.as_view(),
        name='admin_examples_work_html_css-del_h1'),
    url(r'admin_examples_work_html_css/del_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH2Delete.as_view(),
        name='admin_examples_work_html_css-del_h2'),
    url(r'admin_examples_work_html_css/del_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH3Delete.as_view(),
        name='admin_examples_work_html_css-del_h3'),
    url(r'admin_examples_work_html_css/del_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH4Delete.as_view(),
        name='admin_examples_work_html_css-del_h4'),
    url(r'admin_examples_work_html_css/del_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssTextDelete.as_view(),
        name='admin_examples_work_html_css-del_text'),
    url(r'admin_examples_work_html_css/update_main_h1/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH1Update.as_view(),
        name='admin_examples_work_html_css-update_h1'),
    url(r'admin_examples_work_html_css/update_main_h2/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH2Update.as_view(),
        name='admin_examples_work_html_css-update_h2'),
    url(r'admin_examples_work_html_css/update_main_h3/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH3Update.as_view(),
        name='admin_examples_work_html_css-update_h3'),
    url(r'admin_examples_work_html_css/update_main_h4/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssH4Update.as_view(),
        name='admin_examples_work_html_css-update_h4'),
    url(r'admin_examples_work_html_css/update_main_text/(?P<pk>[\w]+)/$',
        AdminExamplesHtmlCssTextUpdate.as_view(),
        name='admin_examples_work_html_css-update_text'),
]

# Блок страниц админки для страницы Учёбы:
urlpatterns += [
    url(r'^admin_education/$',
        AdminEducationListView.as_view(),
        name='admin_education'),
    url(r'admin_education/add_main_h1/$',
        AdminEducationH1Create.as_view(),
        name='admin_education-add_h1'),
    url(r'admin_education/add_main_h2/$',
        AdminEducationH2Create.as_view(),
        name='admin_education-add_h2'),
    url(r'admin_education/add_main_h3/$',
        AdminEducationH3Create.as_view(),
        name='admin_education-add_h3'),
    url(r'admin_education/add_main_h4/$',
        AdminEducationH4Create.as_view(),
        name='admin_education-add_h4'),
    url(r'admin_education/add_main_text/$',
        AdminEducationTextCreate.as_view(),
        name='admin_education-add_text'),
    url(r'admin_education/del_main_h1/(?P<pk>[\w]+)/$',
        AdminEducationH1Delete.as_view(),
        name='admin_education-del_h1'),
    url(r'admin_education/del_main_h2/(?P<pk>[\w]+)/$',
        AdminEducationH2Delete.as_view(),
        name='admin_education-del_h2'),
    url(r'admin_education/del_main_h3/(?P<pk>[\w]+)/$',
        AdminEducationH3Delete.as_view(),
        name='admin_education-del_h3'),
    url(r'admin_education/del_main_h4/(?P<pk>[\w]+)/$',
        AdminEducationH4Delete.as_view(),
        name='admin_education-del_h4'),
    url(r'admin_education/del_main_text/(?P<pk>[\w]+)/$',
        AdminEducationTextDelete.as_view(),
        name='admin_education-del_text'),
    url(r'admin_education/update_main_h1/(?P<pk>[\w]+)/$',
        AdminEducationH1Update.as_view(),
        name='admin_education-update_h1'),
    url(r'admin_education/update_main_h2/(?P<pk>[\w]+)/$',
        AdminEducationH2Update.as_view(),
        name='admin_education-update_h2'),
    url(r'admin_education/update_main_h3/(?P<pk>[\w]+)/$',
        AdminEducationH3Update.as_view(),
        name='admin_education-update_h3'),
    url(r'admin_education/update_main_h4/(?P<pk>[\w]+)/$',
        AdminEducationH4Update.as_view(),
        name='admin_education-update_h4'),
    url(r'admin_education/update_main_text/(?P<pk>[\w]+)/$',
        AdminEducationTextUpdate.as_view(),
        name='admin_education-update_text'),
]

# Блок страниц админки для страницы Работы:
urlpatterns += [
    url(r'^admin_works/$',
        AdminWorksListView.as_view(),
        name='admin_works'),
    url(r'admin_works/add_main_h1/$',
        AdminWorksH1Create.as_view(),
        name='admin_works-add_h1'),
    url(r'admin_works/add_main_h2/$',
        AdminWorksH2Create.as_view(),
        name='admin_works-add_h2'),
    url(r'admin_works/add_main_h3/$',
        AdminWorksH3Create.as_view(),
        name='admin_works-add_h3'),
    url(r'admin_works/add_main_h4/$',
        AdminWorksH4Create.as_view(),
        name='admin_works-add_h4'),
    url(r'admin_works/add_main_text/$',
        AdminWorksTextCreate.as_view(),
        name='admin_works-add_text'),
    url(r'admin_works/del_main_h1/(?P<pk>[\w]+)/$',
        AdminWorksH1Delete.as_view(),
        name='admin_works-del_h1'),
    url(r'admin_works/del_main_h2/(?P<pk>[\w]+)/$',
        AdminWorksH2Delete.as_view(),
        name='admin_works-del_h2'),
    url(r'admin_works/del_main_h3/(?P<pk>[\w]+)/$',
        AdminWorksH3Delete.as_view(),
        name='admin_works-del_h3'),
    url(r'admin_works/del_main_h4/(?P<pk>[\w]+)/$',
        AdminWorksH4Delete.as_view(),
        name='admin_works-del_h4'),
    url(r'admin_works/del_main_text/(?P<pk>[\w]+)/$',
        AdminWorksTextDelete.as_view(),
        name='admin_works-del_text'),
    url(r'admin_works/update_main_h1/(?P<pk>[\w]+)/$',
        AdminWorksH1Update.as_view(),
        name='admin_works-update_h1'),
    url(r'admin_works/update_main_h2/(?P<pk>[\w]+)/$',
        AdminWorksH2Update.as_view(),
        name='admin_works-update_h2'),
    url(r'admin_works/update_main_h3/(?P<pk>[\w]+)/$',
        AdminWorksH3Update.as_view(),
        name='admin_works-update_h3'),
    url(r'admin_works/update_main_h4/(?P<pk>[\w]+)/$',
        AdminWorksH4Update.as_view(),
        name='admin_works-update_h4'),
    url(r'admin_works/update_main_text/(?P<pk>[\w]+)/$',
        AdminWorksTextUpdate.as_view(),
        name='admin_works-update_text'),
]
